import graphene
from django.contrib.auth.models import User

from api_graphql.utils import get_paginator, get_offset, get_public_posts, get_public_episodes
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
        return get_public_episodes(post.episodes)

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
        return get_public_episodes(show.episodes)

    @staticmethod
    def resolve_posts(show, info):
        return get_public_posts(show.posts)

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
        return get_public_posts(user.publications)

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

    all_shows = graphene.List(ShowType, offset=graphene.Int(), count=graphene.Int())

    episode = graphene.Field(EpisodeType, id=graphene.Int())

    all_episodes = graphene.List(EpisodeType, offset=graphene.Int(), count=graphene.Int())

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
    def resolve_all_shows(root, info, offset=0, count=None):
        shows = Show.objects.all()
        return get_offset(shows, offset, count)

    @staticmethod
    def resolve_episode(root, info, id):
        return get_public_episodes(Episode.objects).get(pk=id)

    @staticmethod
    def resolve_all_episodes(root, info, offset=0, count=None):
        episodes = get_public_episodes(Episode.objects)
        return get_offset(episodes, offset, count)

    @staticmethod
    def resolve_post(root, info, id=None, slug=None):
        post = get_public_posts(Post.objects)
        if id:
            return post.get(pk=id)
        return post.get(slug=slug)

    @staticmethod
    def resolve_all_posts(root, info, offset=0, count=None):
        posts = get_public_posts(Post.objects)
        return get_offset(posts, offset, count)

    # DEPRECATED
    @staticmethod
    def resolve_front_page_posts(root, info):
        return get_public_posts(Post.objects)[:30]

    # DEPRECATED
    @staticmethod
    def resolve_paginated_posts(self, info, page, page_size=10):
        qs = get_public_posts(Post.objects)
        return get_paginator(qs, page_size, page, PostPaginatedType)

    @staticmethod
    def resolve_user(root, info, id):
        return User.objects.get(pk=id)

    @staticmethod
    def resolve_all_users(root, info):
        return User.objects.all()


schema = graphene.Schema(query=Query)
