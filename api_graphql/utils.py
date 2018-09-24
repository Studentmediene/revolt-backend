from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# A little helper function, becase we will potentially have many PaginatedTypes
# and we will potentially want to turn many querysets into paginated results:


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
