import requests

RR_API_BASE = 'https://api.radiorevolt.no/v2'


def get_shows():
    r = requests.get(
        '{base}/programmer/list'.format(base=RR_API_BASE),
        timeout=29.
    )
    r.raise_for_status()

    return r.json()
