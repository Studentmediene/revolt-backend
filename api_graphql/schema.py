import graphene
from django.contrib.auth.models import User
from django.utils import timezone

from api_graphql.utils import get_paginator
from data_models.crop import CropImages
from data_models.models import Category, Episode, Post, Settings, Show


class CategoryType(graphene.ObjectType):
    """
    Category description
    """

    id = graphene.Int()
    name = graphene.String()
    text_color = graphene.String()
    background_color = graphene.String()


class SettingsType(graphene.ObjectType):

    id = graphene.Int()
    about = graphene.String()
    chief_editor = graphene.String()
    radio_editor = graphene.String()
    privacy_policy = graphene.String()


class PostType(graphene.ObjectType):
    """
    Post description
    """

    id = graphene.Int()
    title = graphene.String()
    slug = graphene.String()
    image = graphene.String()
    cropped_images = graphene.Field(lambda: CroppedImagesType)
    lead = graphene.String()
    content = graphene.String()
    categories = graphene.List(lambda: CategoryType)
    deleted = graphene.Boolean()
    episodes = graphene.List(lambda: EpisodeType)

    show = graphene.Field(lambda: ShowType)

    publish_at = graphene.String()
    created_at = graphene.String()
    updated_at = graphene.String()
    created_by = graphene.Field(lambda: UserType)

    @staticmethod
    def resolve_show(post, info):
        return post.show

    @staticmethod
    def resolve_categories(post, info):
        return post.categories.all()

    @staticmethod
    def resolve_episodes(post, info):
        return post.episodes.all()

    @staticmethod
    def resolve_created_by(post, info):
        return post.created_by

    @staticmethod
    def resolve_cropped_images(post, info):
        return CropImages(post.image, post.cropping)


class PostPaginatedType(graphene.ObjectType):
    page = graphene.Int()
    pages = graphene.Int()
    has_next = graphene.Boolean()
    has_prev = graphene.Boolean()
    posts = graphene.List(PostType)


class ShowType(graphene.ObjectType):
    """
    Show description
    """

    id = graphene.Int()
    name = graphene.String()
    digas_show_id = graphene.Int()
    image = graphene.String()
    lead = graphene.String()
    content = graphene.String()
    categories = graphene.List(lambda: CategoryType)

    slug = graphene.String()
    archived = graphene.Boolean()

    created_at = graphene.String()
    updated_at = graphene.String()
    created_by = graphene.Field(lambda: UserType)

    episodes = graphene.List(lambda: EpisodeType)

    posts = graphene.List(lambda: PostType)

    @staticmethod
    def resolve_created_by(show, info):
        return show.created_by

    @staticmethod
    def resolve_categories(show, info):
        return show.categories.all()

    @staticmethod
    def resolve_episodes(show, info):
        return show.episodes \
            .order_by('-publish_at') \
            .filter(publish_at__lte=timezone.now())

    @staticmethod
    def resolve_posts(show, info):
        return show.posts.order_by('-created_at')

    @staticmethod
    def resolve_image(show, info):
        return show.image.url


class EpisodeType(graphene.ObjectType):
    """
    Episode description
    """

    id = graphene.Int()
    title = graphene.String()
    lead = graphene.String()
    digas_broadcast_id = graphene.Int()
    digas_show_id = graphene.Int()
    categories = graphene.List(lambda: CategoryType)

    show = graphene.Field(lambda: ShowType)

    created_at = graphene.String()
    updated_at = graphene.String()
    publish_at = graphene.String()
    created_by = graphene.Field(lambda: UserType)

    podcast_url = graphene.String()
    on_demand_url = graphene.String()

    @staticmethod
    def resolve_title(episode, info):
        if episode.use_title:
            return episode.title
        else:
            return '{} {}'.format(episode.show.name, episode.created_at.strftime('%d.%m.%Y'))

    @staticmethod
    def resolve_created_by(episode, info):
        return episode.created_by

    @staticmethod
    def resolve_categories(episode, info):
        return episode.categories.all()

    @staticmethod
    def resolve_show(episode, info):
        return episode.show


class UserType(graphene.ObjectType):
    """
    User description
    """

    id = graphene.Int()
    full_name = graphene.String()

    publications = graphene.List(lambda: PostType)

    @staticmethod
    def resolve_publications(user, info):
        return user.publications.order_by('-created_at')

    @staticmethod
    def resolve_full_name(user, info):
        return user.get_full_name()


class CroppedImagesType(graphene.ObjectType):
    """
    Cropped versions of an image
    """

    large = graphene.String()
    medium = graphene.String()
    small = graphene.String()
    thumbnail = graphene.String()


class Query(graphene.ObjectType):
    """
    Radio Revolt query description
    """
    name = 'Query'

    category = graphene.Field(CategoryType, id=graphene.Int())

    all_categories = graphene.List(CategoryType)

    settings = graphene.Field(SettingsType)

    show = graphene.Field(ShowType, id=graphene.Int(), slug=graphene.String())

    all_shows = graphene.List(ShowType)

    episode = graphene.Field(EpisodeType, id=graphene.Int())

    all_episodes = graphene.List(EpisodeType)

    post = graphene.Field(PostType, id=graphene.Int(), slug=graphene.String())

    all_posts = graphene.List(PostType, offset=graphene.Int(), count=graphene.Int())

    # DEPRECATED
    paginated_posts = graphene.Field(
        PostPaginatedType, page=graphene.Int(), page_size=graphene.Int())

    # DEPRECATED
    front_page_posts = graphene.List(PostType)

    user = graphene.Field(UserType, id=graphene.Int())

    all_users = graphene.List(UserType)

    cropped_images = graphene.Field(CroppedImagesType)

    @staticmethod
    def resolve_category(root, info, id):
        return Category.objects.get(pk=id)

    @staticmethod
    def resolve_all_categories(root, info):
        return Category.objects.all()

    @staticmethod
    def resolve_settings(root, info):
        return Settings.get_solo()

    @staticmethod
    def resolve_show(root, info, id=None, slug=None):
        if id:
            return Show.objects.get(pk=id)
        return Show.objects.get(slug=slug)

    @staticmethod
    def resolve_all_shows(root, info):
        return Show.objects.all()

    @staticmethod
    def resolve_episode(root, info, id):
        episode = Episode.objects.get(pk=id)
        if episode.publish_at >= timezone.now():
            raise Episode.DoesNotExist('Episode matching query does not exist.')
        else:
            return episode

    @staticmethod
    def resolve_all_episodes(root, info):
        return Episode.objects \
            .order_by('-publish_at') \
            .filter(publish_at__lte=timezone.now())

    @staticmethod
    def resolve_post(root, info, id=None, slug=None):
        post = Post.objects \
            .filter(publish_at__lte=timezone.now()) \
            .filter(ready_to_be_published=True)
        if id:
            return post.get(pk=id)
        else:
            return post.get(slug=slug)

    @staticmethod
    def resolve_all_posts(root, info, offset=0, count=None):
        posts = Post.objects \
            .order_by('-publish_at') \
            .filter(publish_at__lte=timezone.now()) \
            .filter(ready_to_be_published=True)
        if count:
            return posts[offset:offset + count]
        else:
            return posts[offset:]

    # DEPRECATED
    @staticmethod
    def resolve_front_page_posts(root, info):
        return Post.objects \
            .order_by('-publish_at') \
            .filter(publish_at__lte=timezone.now()) \
            .filter(ready_to_be_published=True)[:30]

    # DEPRECATED
    @staticmethod
    def resolve_paginated_posts(self, info, page, page_size=10):
        qs = Post.objects \
            .order_by('-publish_at') \
            .filter(publish_at__lte=timezone.now()) \
            .filter(ready_to_be_published=True)
        return get_paginator(qs, page_size, page, PostPaginatedType)

    @staticmethod
    def resolve_user(root, info, id):
        return User.objects.get(pk=id)

    @staticmethod
    def resolve_all_users(root, info):
        return User.objects.all()


schema = graphene.Schema(query=Query)
