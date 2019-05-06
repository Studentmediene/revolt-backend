import pytest
import requests
from django.conf import settings
from django.contrib import admin as django_admin
from django.core.management import call_command
from django.urls import reverse

from data_models import admin
from data_models.models import Show
from data_models.rr_api import get_podcast_url_from_digas_id


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


mocked_show_list = [
    {
        'old': 0,
        'id': 123,
        'name': 'Program1'
    },
    {
        'old': 1,
        'id': 234,
        'name': 'Program2'
    },
    {
        'old': 0,
        'id': 345,
        'name': 'Program3'
    },
    {
        'old': 0,
        'id': 456,
        'name': 'Program4'
    },
]


@pytest.mark.django_db
def test_admin_show_details(admin_client, requests_mock):
    requests_mock.get('{}/programmer/list'.format(settings.RR_API_BASE), json=mocked_show_list)
    response = admin_client.get('/admin/data_models/show/1/change/')

    assert response.status_code == 200


@pytest.mark.django_db
def test_admin_show_details_on_error(admin_client, requests_mock):
    requests_mock.get(
        '{}/programmer/list'.format(settings.RR_API_BASE),
        exc=requests.HTTPError('A simulated error occurred, but it should not hinder page render.'),
    )
    response = admin_client.get('/admin/data_models/show/1/change/')

    assert response.status_code == 200

    # Was a request made?
    assert requests_mock.call_count == 1

    # Timeout should be set for all requests in production
    timeout = requests_mock.last_request.timeout
    assert timeout is not None
    assert timeout > 0


@pytest.mark.django_db
def test_admin_episode_details(admin_client):
    response = admin_client.get('/admin/data_models/episode/1/change/')

    assert response.status_code == 200


@pytest.mark.django_db
def test_admin_post_details(admin_client):
    response = admin_client.get('/admin/data_models/post/1/change/')

    assert response.status_code == 200


program1_podcast_url = 'http://podkast.radiorevolt.no/program1'
old_podcast_url = 'http://example.com/outdated_url'


@pytest.mark.django_db
@pytest.mark.parametrize('digas_id,podcast_url,mocked_response', [
    (123, program1_podcast_url, {
        'text': program1_podcast_url
    }),
    (234, None, {
        'status_code': 404,
        'reason': 'Not Found'
    }),
    (234, old_podcast_url, {
        'exc': requests.HTTPError('This is a simulated error')
    }),
    (None, None, None),
])
def test_populating_podcast_url(requests_mock, digas_id, podcast_url, mocked_response):
    # Mock the podcast API
    if digas_id is not None:
        expected_url = '{}/url/{}'.format(settings.PODCAST_API_BASE, digas_id)
        requests_mock.get(expected_url, **mocked_response)

    assert not requests_mock.called

    # Trigger code for updating podcast URL
    for index, show in enumerate(Show.objects.filter(digas_id=digas_id)):
        show.podcast_url = old_podcast_url
        show.save()

        assert show.podcast_url == podcast_url

        if digas_id is None:
            # No request should have been made
            assert not requests_mock.called
        else:
            # Was a new request made?
            assert requests_mock.call_count == index + 1

            # All requests should have timeout assigned
            timeout = requests_mock.last_request.timeout
            assert timeout is not None
            assert requests_mock.last_request.timeout > 0


def test_giving_none_to_podcast_api(requests_mock):
    # The model doesn't call the API function when digas_id is None, so we must test that ourselves
    assert get_podcast_url_from_digas_id(None) is None
    assert not requests_mock.called


def test_show_admin_form(requests_mock):
    # We do not mock any requests, therefore the requests will fail and trigger the path we test
    test_data = {
        'content': '<p>This is some content</p>',
        'digas_id': '234',
        'name': 'Program1',
        'lead': 'Hei der',
    }
    form = admin.ShowAdminForm(test_data)
    choices = form.fields['digas_id'].choices
    assert len(choices) == 1
    assert choices[0][0] == test_data['digas_id']

    del test_data['digas_id']
    form = admin.ShowAdminForm(test_data)
    choices = form.fields['digas_id'].choices
    assert len(choices) == 1
    assert not choices[0][0]


@pytest.mark.django_db
@pytest.mark.parametrize('action,is_podcast', [('make_podcast', True), ('unmake_podcast', False)])
def test_is_podcast_actions(requests_mock, admin_client, action, is_podcast):
    num_shows = Show.objects.count()
    assert Show.objects.filter(is_podcast=is_podcast).count() != num_shows

    change_url = reverse('admin:data_models_show_changelist')
    shows = Show.objects.all()
    data = {'action': action, django_admin.ACTION_CHECKBOX_NAME: shows.values_list('pk', flat=True)}

    response = admin_client.post(change_url, data=data, follow=True)

    assert response.status_code == 200
    assert Show.objects.filter(is_podcast=is_podcast).count() == num_shows
