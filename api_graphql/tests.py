import pytest
from django.core.management import call_command
from graphene.test import Client

from api_graphql.schema import schema


@pytest.fixture(scope='session')
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command('loaddata', 'test_fixtures.json')


@pytest.mark.django_db
def test_category_by_id(snapshot):
    client = Client(schema)
    executed = client.execute('''query {
        category(id:1) {
            id,
            name,
            textColor,
            backgroundColor
        }
    }''')

    snapshot.assert_match(executed)


@pytest.mark.django_db
def test_all_categories(snapshot):
    client = Client(schema)
    executed = client.execute('''query {
        allCategories {
            id,
            name,
            textColor,
            backgroundColor
        }
    }''')

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


@pytest.mark.django_db
def test_show_by_id(snapshot):
    client = Client(schema)
    executed = client.execute('''query {
        show(id:1) {
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
    }''')

    snapshot.assert_match(executed)


@pytest.mark.django_db
def test_show_by_slug(snapshot):
    client = Client(schema)
    executed = client.execute('''query {
        show(slug:"program2") {
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
    }''')

    snapshot.assert_match(executed)


@pytest.mark.django_db
def test_all_shows(snapshot):
    client = Client(schema)
    executed = client.execute('''query {
            allShows {
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
        }''')

    snapshot.assert_match(executed)


@pytest.mark.django_db
def test_all_shows_with_offset(snapshot):
    client = Client(schema)
    executed = client.execute('''query {
            allShows(offset: 1) {
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
        }''')

    snapshot.assert_match(executed)


@pytest.mark.django_db
def test_all_shows_with_count(snapshot):
    client = Client(schema)
    executed = client.execute('''query {
            allShows(offset: 2, count:2) {
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
        }''')

    snapshot.assert_match(executed)


@pytest.mark.django_db
def test_episode_by_id(snapshot):
    client = Client(schema)
    executed = client.execute('''query {
        episode(id:1) {
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
    }''')

    snapshot.assert_match(executed)


@pytest.mark.django_db
def test_all_episodes(snapshot):
    client = Client(schema)
    executed = client.execute('''query {
        allEpisodes {
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
    }''')

    snapshot.assert_match(executed)


@pytest.mark.django_db
def test_all_episodes_with_offset(snapshot):
    client = Client(schema)
    executed = client.execute('''query {
        allEpisodes(offset:1) {
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
    }''')

    snapshot.assert_match(executed)


@pytest.mark.django_db
def test_all_episodes_with_count(snapshot):
    client = Client(schema)
    executed = client.execute('''query {
        allEpisodes(offset:1,count:2) {
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
    }''')

    snapshot.assert_match(executed)


@pytest.mark.django_db
def test_post_by_id(snapshot):
    client = Client(schema)
    executed = client.execute('''query {
        post(id:2) {
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
    }''')

    snapshot.assert_match(executed)


@pytest.mark.django_db
def test_post_by_slug(snapshot):
    client = Client(schema)
    executed = client.execute('''query {
        post(slug:"den-forste-artikkelen") {
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
    }''')

    snapshot.assert_match(executed)


@pytest.mark.django_db
def test_all_posts(snapshot):
    client = Client(schema)
    executed = client.execute('''query {
        allPosts {
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
    }''')

    snapshot.assert_match(executed)


@pytest.mark.django_db
def test_all_posts_with_offset(snapshot):
    client = Client(schema)
    executed = client.execute('''query {
        allPosts(offset:3) {
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
    }''')

    snapshot.assert_match(executed)


@pytest.mark.django_db
def test_all_posts_with_count(snapshot):
    client = Client(schema)
    executed = client.execute('''query {
        allPosts(offset:3,count:5) {
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
    }''')

    snapshot.assert_match(executed)


@pytest.mark.django_db
def test_user_by_id(snapshot):
    client = Client(schema)
    executed = client.execute('''query {
        user(id:1) {
            id
            fullName
            publications {
                id
            }
        }
    }''')
    snapshot.assert_match(executed)


@pytest.mark.django_db
def test_all_users(snapshot):
    client = Client(schema)
    executed = client.execute('''query {
        allUsers {
            id
            fullName
            publications {
                id
            }
        }
    }''')
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
