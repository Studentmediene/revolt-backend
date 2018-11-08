import pytest
from django.core.management import call_command
from graphene.test import Client

from api_graphql.schema import schema


def assert_query(snapshot, query, model_name):
    client = Client(schema)
    executed = client.execute(query.replace('MODEL_NAME', model_name))
    snapshot.assert_match(executed)


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
    assert_query(snapshot, category_query, 'category(id:1)')


@pytest.mark.django_db
def test_all_categories(snapshot):
    assert_query(snapshot, category_query, 'allCategories')


settings_query = '''query {
    MODEL_NAME {
        chiefEditor,
        about,
        radioEditor,
        privacyPolicy,
    }
}'''


@pytest.mark.django_db
def test_settings(snapshot):
    assert_query(snapshot, settings_query, 'settings')


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
    assert_query(snapshot, show_query, 'show(id:1)')


@pytest.mark.django_db
def test_show_by_slug(snapshot):
    assert_query(snapshot, show_query, 'show(slug:"program2")')


@pytest.mark.django_db
def test_all_shows(snapshot):
    client = Client(schema)
    executed = client.execute(show_query.replace('MODEL_NAME', 'allShows'))
    snapshot.assert_match(executed)


@pytest.mark.django_db
def test_all_shows_with_offset(snapshot):
    assert_query(snapshot, show_query, 'allShows(offset: 1)')


@pytest.mark.django_db
def test_all_shows_with_count(snapshot):
    assert_query(snapshot, show_query, 'allShows(offset: 2, count:2)')


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
    assert_query(snapshot, episode_query, 'episode(id:1)')


@pytest.mark.django_db
def test_all_episodes(snapshot):
    assert_query(snapshot, episode_query, 'allEpisodes')


@pytest.mark.django_db
def test_all_episodes_with_offset(snapshot):
    assert_query(snapshot, episode_query, 'allEpisodes(offset:1)')


@pytest.mark.django_db
def test_all_episodes_with_count(snapshot):
    assert_query(snapshot, episode_query, 'allEpisodes(offset:1,count:2)')


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
    assert_query(snapshot, post_query, 'post(id:2)')


@pytest.mark.django_db
def test_post_by_slug(snapshot):
    assert_query(snapshot, post_query, 'post(slug:"den-forste-artikkelen")')


@pytest.mark.django_db
def test_all_posts(snapshot):
    assert_query(snapshot, post_query, 'allPosts')


@pytest.mark.django_db
def test_all_posts_with_offset(snapshot):
    assert_query(snapshot, post_query, 'allPosts(offset:3)')


@pytest.mark.django_db
def test_all_posts_with_count(snapshot):
    assert_query(snapshot, post_query, 'allPosts(offset:3,count:5)')


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
    assert_query(snapshot, user_query, 'user(id:1)')


@pytest.mark.django_db
def test_all_users(snapshot):
    assert_query(snapshot, user_query, 'allUsers')


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
