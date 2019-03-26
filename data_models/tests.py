import pytest
from django.core.management import call_command


@pytest.fixture(scope='session')
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command('loaddata', 'test_fixtures.json')


@pytest.mark.django_db
def test_admin_index(admin_client):
    response = admin_client.get('/admin/')

    assert response.status_code == 200


@pytest.mark.django_db
def test_admin_post(admin_client):
    response = admin_client.get('/admin/data_models/post/')

    assert response.status_code == 200


@pytest.mark.django_db
def test_admin_show(admin_client):
    response = admin_client.get('/admin/data_models/show/')

    assert response.status_code == 200


@pytest.mark.django_db
def test_admin_episode(admin_client):
    response = admin_client.get('/admin/data_models/episode/')

    assert response.status_code == 200


@pytest.mark.django_db
def test_admin_settings(admin_client):
    response = admin_client.get('/admin/data_models/settings/')

    assert response.status_code == 200


@pytest.mark.django_db
def test_admin_highlightedposts(admin_client):
    response = admin_client.get('/admin/data_models/highlightedpost/')

    assert response.status_code == 200


@pytest.mark.django_db
def test_admin_show_details(admin_client):
    response = admin_client.get('/admin/data_models/show/1/change/')

    assert response.status_code == 200


@pytest.mark.django_db
def test_admin_episode_details(admin_client):
    response = admin_client.get('/admin/data_models/episode/1/change/')

    assert response.status_code == 200


@pytest.mark.django_db
def test_admin_post_details(admin_client):
    response = admin_client.get('/admin/data_models/post/1/change/')

    assert response.status_code == 200
