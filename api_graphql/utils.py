from datetime import timedelta

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.utils import timezone


# A little helper function, becase we will potentially have many PaginatedTypes
# and we will potentially want to turn many querysets into paginated results:
# DEPRECATED
def get_paginator(qs, page_size, page, paginated_type, **kwargs):
    p = Paginator(qs, page_size)
    try:
        page_obj = p.page(page)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    return paginated_type(
        page=page_obj.number,
        pages=p.num_pages,
        has_next=page_obj.has_next(),
        has_prev=page_obj.has_previous(),
        posts=page_obj.object_list,
        **kwargs)


def get_offset(qs, offset, count):
    if count:
        return qs[offset:offset + count]
    else:
        return qs[offset:]


def get_public_posts(posts):
    return posts \
        .order_by('-publish_at') \
        .filter(publish_at__lte=timezone.now()) \
        .filter(deleted=False) \
        .filter(ready_to_be_published=True)


def get_public_episodes(episodes):
    return episodes \
        .order_by('-publish_at') \
        .filter(publish_at__lte=timezone.now()) \
        .filter(publish_at__gte=timezone.now() - timedelta(days=730))
    # Hide all episodes that are older than 2 years, because of license rights through TONO.
    # We are not allowed to make old episodes with music available. In the future we are hopefully
    # allowed to serve old episodes with music.
