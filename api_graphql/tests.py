import pytest
from django.core.management import call_command
from graphene.test import Client

from api_graphql.schema import schema


@pytest.fixture(scope='session')
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command('loaddata', 'test_fixtures.json')


category_query = '''query {
    MODEL_NAME {
        id,
        name,
        textColor,
        backgroundColor
    }
}'''


@pytest.mark.django_db
def test_category_by_id(snapshot):
    client = Client(schema)
    executed = client.execute(category_query.replace('MODEL_NAME', 'category(id:1)'))
    snapshot.assert_match(executed)


@pytest.mark.django_db
def test_all_categories(snapshot):
    client = Client(schema)
    executed = client.execute(category_query.replace('MODEL_NAME', 'allCategories'))
    snapshot.assert_match(executed)


@pytest.mark.django_db
def test_settings(snapshot):
    client = Client(schema)
    executed = client.execute('''query {
        settings {
            chiefEditor,
            about,
            radioEditor,
            privacyPolicy,
        }
    }''')
    snapshot.assert_match(executed)


show_query = '''query {
    MODEL_NAME {
        id
        name
        digasShowId
        image
        lead
        content
        categories {
            id
        }
        slug
        archived
        createdAt
        updatedAt
        createdBy {
            id
        }
        episodes {
            id
        }
        posts {
            id
        }
    }
}'''


@pytest.mark.django_db
def test_show_by_id(snapshot):
    client = Client(schema)
    executed = client.execute(show_query.replace('MODEL_NAME', 'show(id:1)'))
    snapshot.assert_match(executed)


@pytest.mark.django_db
def test_show_by_slug(snapshot):
    client = Client(schema)
    executed = client.execute(show_query.replace('MODEL_NAME', 'show(slug:"program2")'))
    snapshot.assert_match(executed)


@pytest.mark.django_db
def test_all_shows(snapshot):
    client = Client(schema)
    executed = client.execute(show_query.replace('MODEL_NAME', 'allShows'))
    snapshot.assert_match(executed)


@pytest.mark.django_db
def test_all_shows_with_offset(snapshot):
    client = Client(schema)
    executed = client.execute(show_query.replace('MODEL_NAME', 'allShows(offset: 1)'))
    snapshot.assert_match(executed)


@pytest.mark.django_db
def test_all_shows_with_count(snapshot):
    client = Client(schema)
    executed = client.execute(show_query.replace('MODEL_NAME', 'allShows(offset: 2, count:2)'))
    snapshot.assert_match(executed)


episode_query = '''query {
    MODEL_NAME {
        id
        title
        lead
        digasBroadcastId
        digasShowId
        categories {
            id
        }
        show {
            id
        }
        createdAt
        updatedAt
        publishAt
        createdBy {
            id
        }
        podcastUrl
        onDemandUrl
    }
}'''


@pytest.mark.django_db
def test_episode_by_id(snapshot):
    client = Client(schema)
    executed = client.execute(episode_query.replace('MODEL_NAME', 'episode(id:1)'))
    snapshot.assert_match(executed)


@pytest.mark.django_db
def test_all_episodes(snapshot):
    client = Client(schema)
    executed = client.execute(episode_query.replace('MODEL_NAME', 'allEpisodes'))
    snapshot.assert_match(executed)


@pytest.mark.django_db
def test_all_episodes_with_offset(snapshot):
    client = Client(schema)
    executed = client.execute(episode_query.replace('MODEL_NAME', 'allEpisodes(offset:1)'))
    snapshot.assert_match(executed)


@pytest.mark.django_db
def test_all_episodes_with_count(snapshot):
    client = Client(schema)
    executed = client.execute(episode_query.replace('MODEL_NAME', 'allEpisodes(offset:1,count:2)'))
    snapshot.assert_match(executed)


post_query = '''query {
    MODEL_NAME {
        id
        title
        slug
        image
        croppedImages {
            large
            medium
            small
            thumbnail
        }
        lead
        content
        categories {
            id
        }
        deleted
        episodes {
            id
        }
        show {
            id
        }
        publishAt
        createdBy {
            id
        }
    }
}'''


@pytest.mark.django_db
def test_post_by_id(snapshot):
    client = Client(schema)
    executed = client.execute(post_query.replace('MODEL_NAME', 'post(id:2)'))
    snapshot.assert_match(executed)


@pytest.mark.django_db
def test_post_by_slug(snapshot):
    client = Client(schema)
    executed = client.execute(
        post_query.replace('MODEL_NAME', 'post(slug:"den-forste-artikkelen")'))
    snapshot.assert_match(executed)


@pytest.mark.django_db
def test_all_posts(snapshot):
    client = Client(schema)
    executed = client.execute(post_query.replace('MODEL_NAME', 'allPosts'))
    snapshot.assert_match(executed)


@pytest.mark.django_db
def test_all_posts_with_offset(snapshot):
    client = Client(schema)
    executed = client.execute(post_query.replace('MODEL_NAME', 'allPosts(offset:3)'))
    snapshot.assert_match(executed)


@pytest.mark.django_db
def test_all_posts_with_count(snapshot):
    client = Client(schema)
    executed = client.execute(post_query.replace('MODEL_NAME', 'allPosts(offset:3,count:5)'))
    snapshot.assert_match(executed)


user_query = '''query {
    MODEL_NAME {
        id
        fullName
        publications {
            id
        }
    }
}'''


@pytest.mark.django_db
def test_user_by_id(snapshot):
    client = Client(schema)
    executed = client.execute(user_query.replace('MODEL_NAME', 'user(id:1)'))
    snapshot.assert_match(executed)


@pytest.mark.django_db
def test_all_users(snapshot):
    client = Client(schema)
    executed = client.execute(user_query.replace('MODEL_NAME', 'allUsers'))
    snapshot.assert_match(executed)


# DEPRECATED
@pytest.mark.django_db
def test_frontpage(snapshot):
    client = Client(schema)
    executed = client.execute('''query {
        frontPagePosts {
            id,
            title,
            slug,
            croppedImages {
                large,
                medium,
                small
            },
            lead,
            publishAt,
            categories {
                name,
                textColor,
                backgroundColor
            }
        }
    }''')
    snapshot.assert_match(executed)


# DEPRECATED
@pytest.mark.django_db
def test_paginated_posts(client, snapshot):
    client = Client(schema)
    response = client.execute('''query {
        paginatedPosts(page: 1) {
            hasPrev,
            hasNext,
            pages,
            posts {
                id,
                title,
                slug,
                lead,
                publishAt,
                categories {
                    name,
                    textColor,
                    backgroundColor
                }
            }
        }
    }''')

    snapshot.assert_match(response)
