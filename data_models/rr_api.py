import logging

import requests
from django.conf import settings

log = logging.getLogger(__name__)

RR_API_BASE = settings.RR_API_BASE
PODCAST_API_BASE = settings.PODCAST_API_BASE


def get_shows():
    r = requests.get('{base}/programmer/list'.format(base=RR_API_BASE), timeout=29.)
    r.raise_for_status()

    return r.json()


def get_podcast_url_from_digas_id(digas_id):
    if digas_id is None:
        # Short-circuit when no ID exists
        return None

    url = '{base}/url/{digas_id}'.format(base=PODCAST_API_BASE, digas_id=digas_id)
    r = requests.get(url, timeout=5.)
    if r.status_code == 404:
        # 404 is used to indicate that the ID was not found
        log.warning('Digas ID {digas_id} not found when querying podcast API at {url}, '
                    'or podcast API base has been set incorrectly'.format(
                        digas_id=digas_id, url=url))
        return None

    # Any other error status code is an unexpected error
    r.raise_for_status()

    # Good, we have a URL!
    return r.text
