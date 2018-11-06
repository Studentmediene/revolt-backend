# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_post_by_slug 1'] = {
    'data': {
        'post': {
            'categories': [
                {
                    'id': 1
                }
            ],
            'content': '<p><b>Her</b> har vi teksten!</p>',
            'createdBy': {
                'id': 2
            },
            'croppedImages': {
                'large': '/media/cache/9c/7e/9c7ec938cac65a0bac80a67542ccf3af.jpg',
                'medium': '/media/cache/0d/c6/0dc6a4cee46602608c70347932545628.jpg',
                'small': '/media/cache/00/f2/00f21860fb35fef4b16ed402b407f846.jpg',
                'thumbnail': '/media/cache/8e/8f/8e8fdbe3d759e3591c21d7d73effe9b6.jpg'
            },
            'deleted': False,
            'episodes': [
                {
                    'id': 1
                }
            ],
            'id': 1,
            'image': 'uploads/images/700x350.png',
            'lead': 'Ingressen her',
            'publishAt': '2018-02-23 21:31:29+00:00',
            'show': None,
            'slug': 'den-forste-artikkelen',
            'title': 'Den første artikkelen'
        }
    }
}

snapshots['test_settings 1'] = {
    'data': {
        'settings': {
            'about': '<p>About text</p>',
            'chiefEditor': 'chief editor',
            'privacyPolicy': '<div>privacy policy </div>',
            'radioEditor': 'radio editor'
        }
    }
}

snapshots['test_episode_by_id 1'] = {
    'data': {
        'episode': {
            'categories': [
                {
                    'id': 1
                }
            ],
            'createdAt': '2018-02-23 21:30:49.252000+00:00',
            'createdBy': {
                'id': 2
            },
            'digasBroadcastId': None,
            'digasShowId': None,
            'id': 1,
            'lead': 'Dette er en episode',
            'onDemandUrl': 'http://example.com/lyd.mp3',
            'podcastUrl': None,
            'publishAt': '2018-02-23 21:30:14+00:00',
            'show': {
                'id': 1
            },
            'title': 'Program1 23.02.2018',
            'updatedAt': '2018-02-23 21:30:49.252000+00:00'
        }
    }
}

snapshots['test_show_by_slug 1'] = {
    'data': {
        'show': {
            'archived': False,
            'categories': [
            ],
            'content': '<p>Program2 lenger beskrivelse!</p>',
            'createdAt': '2018-02-23 21:29:54.395000+00:00',
            'createdBy': {
                'id': 2
            },
            'digasShowId': None,
            'episodes': [
                {
                    'id': 2
                }
            ],
            'id': 2,
            'image': '/media/uploads/images/300x300_9U7yu4U.png',
            'lead': 'Program2 beskrivelse',
            'name': 'Program2',
            'posts': [
                {
                    'id': 2
                }
            ],
            'slug': 'program2',
            'updatedAt': '2018-02-23 21:29:54.395000+00:00'
        }
    }
}

snapshots['test_all_shows 1'] = {
    'data': {
        'allShows': [
            {
                'archived': False,
                'categories': [
                ],
                'content': '<p>Program1 lenger beskrivelse</p>',
                'createdAt': '2018-02-23 21:29:09.247000+00:00',
                'createdBy': {
                    'id': 2
                },
                'digasShowId': None,
                'episodes': [
                    {
                        'id': 1
                    }
                ],
                'id': 1,
                'image': '/media/uploads/images/300x300.png',
                'lead': 'Program1 beskrivelse',
                'name': 'Program1',
                'posts': [
                ],
                'slug': 'program1',
                'updatedAt': '2018-02-23 21:29:09.247000+00:00'
            },
            {
                'archived': False,
                'categories': [
                ],
                'content': '<p>Program2 lenger beskrivelse!</p>',
                'createdAt': '2018-02-23 21:29:54.395000+00:00',
                'createdBy': {
                    'id': 2
                },
                'digasShowId': None,
                'episodes': [
                    {
                        'id': 2
                    }
                ],
                'id': 2,
                'image': '/media/uploads/images/300x300_9U7yu4U.png',
                'lead': 'Program2 beskrivelse',
                'name': 'Program2',
                'posts': [
                    {
                        'id': 2
                    }
                ],
                'slug': 'program2',
                'updatedAt': '2018-02-23 21:29:54.395000+00:00'
            },
            {
                'archived': False,
                'categories': [
                ],
                'content': '<p>Program3 lenger beskrivelse!</p>',
                'createdAt': '2018-03-23 21:29:54.395000+00:00',
                'createdBy': {
                    'id': 2
                },
                'digasShowId': None,
                'episodes': [
                ],
                'id': 3,
                'image': '/media/uploads/images/300x300_9U7yu4U.png',
                'lead': 'Program3 beskrivelse',
                'name': 'Program3',
                'posts': [
                ],
                'slug': 'program3',
                'updatedAt': '2018-03-23 21:29:54.395000+00:00'
            },
            {
                'archived': False,
                'categories': [
                ],
                'content': '<p>Program4 lenger beskrivelse!</p>',
                'createdAt': '2018-03-23 21:29:54.395000+00:00',
                'createdBy': {
                    'id': 2
                },
                'digasShowId': None,
                'episodes': [
                ],
                'id': 4,
                'image': '/media/uploads/images/300x300_9U7yu4U.png',
                'lead': 'Program4 beskrivelse',
                'name': 'Program4',
                'posts': [
                ],
                'slug': 'program4',
                'updatedAt': '2018-03-23 21:29:54.395000+00:00'
            }
        ]
    }
}

snapshots['test_all_categories 1'] = {
    'data': {
        'allCategories': [
            {
                'backgroundColor': '#ECB61C',
                'id': 1,
                'name': 'Radio',
                'textColor': '#000000'
            }
        ]
    }
}

snapshots['test_category_by_id 1'] = {
    'data': {
        'category': {
            'backgroundColor': '#ECB61C',
            'id': 1,
            'name': 'Radio',
            'textColor': '#000000'
        }
    }
}

snapshots['test_paginated_posts 1'] = {
    'data': {
        'paginatedPosts': {
            'hasNext': False,
            'hasPrev': False,
            'pages': 1,
            'posts': [
                {
                    'categories': [
                        {
                            'backgroundColor': '#ECB61C',
                            'name': 'Radio',
                            'textColor': '#000000'
                        }
                    ],
                    'id': 1,
                    'lead': 'Ingressen her',
                    'publishAt': '2018-02-23 21:31:29+00:00',
                    'slug': 'den-forste-artikkelen',
                    'title': 'Den første artikkelen'
                },
                {
                    'categories': [
                        {
                            'backgroundColor': '#ECB61C',
                            'name': 'Radio',
                            'textColor': '#000000'
                        }
                    ],
                    'id': 2,
                    'lead': 'Enda en ingress',
                    'publishAt': '2018-02-23 21:30:30+00:00',
                    'slug': 'den-andre-artikkelen',
                    'title': 'Den andre artikkelen'
                },
                {
                    'categories': [
                        {
                            'backgroundColor': '#ECB61C',
                            'name': 'Radio',
                            'textColor': '#000000'
                        }
                    ],
                    'id': 3,
                    'lead': 'Ingressen her',
                    'publishAt': '2018-02-23 21:29:29+00:00',
                    'slug': 'den-3rd-artikkelen',
                    'title': 'Den tredje artikkelen'
                },
                {
                    'categories': [
                        {
                            'backgroundColor': '#ECB61C',
                            'name': 'Radio',
                            'textColor': '#000000'
                        }
                    ],
                    'id': 7,
                    'lead': 'Ingressen her',
                    'publishAt': '2018-02-23 21:25:29+00:00',
                    'slug': 'den-7th-artikkelen',
                    'title': 'Den syvende artikkelen'
                }
            ]
        }
    }
}

snapshots['test_frontpage 1'] = {
    'data': {
        'frontPagePosts': [
            {
                'categories': [
                    {
                        'backgroundColor': '#ECB61C',
                        'name': 'Radio',
                        'textColor': '#000000'
                    }
                ],
                'croppedImages': {
                    'large': '/media/cache/9c/7e/9c7ec938cac65a0bac80a67542ccf3af.jpg',
                    'medium': '/media/cache/0d/c6/0dc6a4cee46602608c70347932545628.jpg',
                    'small': '/media/cache/00/f2/00f21860fb35fef4b16ed402b407f846.jpg'
                },
                'id': 1,
                'lead': 'Ingressen her',
                'publishAt': '2018-02-23 21:31:29+00:00',
                'slug': 'den-forste-artikkelen',
                'title': 'Den første artikkelen'
            },
            {
                'categories': [
                    {
                        'backgroundColor': '#ECB61C',
                        'name': 'Radio',
                        'textColor': '#000000'
                    }
                ],
                'croppedImages': {
                    'large': '/media/cache/bf/0c/bf0c64d01f8854de77f44e8995bb6263.jpg',
                    'medium': '/media/cache/b3/9c/b39c21c911d5cbfe60192fe818985a7e.jpg',
                    'small': '/media/cache/8f/11/8f11ece1c53c8e55aadaa2cd700edcda.jpg'
                },
                'id': 2,
                'lead': 'Enda en ingress',
                'publishAt': '2018-02-23 21:30:30+00:00',
                'slug': 'den-andre-artikkelen',
                'title': 'Den andre artikkelen'
            },
            {
                'categories': [
                    {
                        'backgroundColor': '#ECB61C',
                        'name': 'Radio',
                        'textColor': '#000000'
                    }
                ],
                'croppedImages': {
                    'large': '/media/cache/9c/7e/9c7ec938cac65a0bac80a67542ccf3af.jpg',
                    'medium': '/media/cache/0d/c6/0dc6a4cee46602608c70347932545628.jpg',
                    'small': '/media/cache/00/f2/00f21860fb35fef4b16ed402b407f846.jpg'
                },
                'id': 3,
                'lead': 'Ingressen her',
                'publishAt': '2018-02-23 21:29:29+00:00',
                'slug': 'den-3rd-artikkelen',
                'title': 'Den tredje artikkelen'
            },
            {
                'categories': [
                    {
                        'backgroundColor': '#ECB61C',
                        'name': 'Radio',
                        'textColor': '#000000'
                    }
                ],
                'croppedImages': {
                    'large': '/media/cache/9c/7e/9c7ec938cac65a0bac80a67542ccf3af.jpg',
                    'medium': '/media/cache/0d/c6/0dc6a4cee46602608c70347932545628.jpg',
                    'small': '/media/cache/00/f2/00f21860fb35fef4b16ed402b407f846.jpg'
                },
                'id': 7,
                'lead': 'Ingressen her',
                'publishAt': '2018-02-23 21:25:29+00:00',
                'slug': 'den-7th-artikkelen',
                'title': 'Den syvende artikkelen'
            }
        ]
    }
}

snapshots['test_all_shows_with_offset 1'] = {
    'data': {
        'allShows': [
            {
                'archived': False,
                'categories': [
                ],
                'content': '<p>Program2 lenger beskrivelse!</p>',
                'createdAt': '2018-02-23 21:29:54.395000+00:00',
                'createdBy': {
                    'id': 2
                },
                'digasShowId': None,
                'episodes': [
                    {
                        'id': 2
                    }
                ],
                'id': 2,
                'image': '/media/uploads/images/300x300_9U7yu4U.png',
                'lead': 'Program2 beskrivelse',
                'name': 'Program2',
                'posts': [
                    {
                        'id': 2
                    }
                ],
                'slug': 'program2',
                'updatedAt': '2018-02-23 21:29:54.395000+00:00'
            },
            {
                'archived': False,
                'categories': [
                ],
                'content': '<p>Program3 lenger beskrivelse!</p>',
                'createdAt': '2018-03-23 21:29:54.395000+00:00',
                'createdBy': {
                    'id': 2
                },
                'digasShowId': None,
                'episodes': [
                ],
                'id': 3,
                'image': '/media/uploads/images/300x300_9U7yu4U.png',
                'lead': 'Program3 beskrivelse',
                'name': 'Program3',
                'posts': [
                ],
                'slug': 'program3',
                'updatedAt': '2018-03-23 21:29:54.395000+00:00'
            },
            {
                'archived': False,
                'categories': [
                ],
                'content': '<p>Program4 lenger beskrivelse!</p>',
                'createdAt': '2018-03-23 21:29:54.395000+00:00',
                'createdBy': {
                    'id': 2
                },
                'digasShowId': None,
                'episodes': [
                ],
                'id': 4,
                'image': '/media/uploads/images/300x300_9U7yu4U.png',
                'lead': 'Program4 beskrivelse',
                'name': 'Program4',
                'posts': [
                ],
                'slug': 'program4',
                'updatedAt': '2018-03-23 21:29:54.395000+00:00'
            }
        ]
    }
}

snapshots['test_all_shows_with_count 1'] = {
    'data': {
        'allShows': [
            {
                'archived': False,
                'categories': [
                ],
                'content': '<p>Program3 lenger beskrivelse!</p>',
                'createdAt': '2018-03-23 21:29:54.395000+00:00',
                'createdBy': {
                    'id': 2
                },
                'digasShowId': None,
                'episodes': [
                ],
                'id': 3,
                'image': '/media/uploads/images/300x300_9U7yu4U.png',
                'lead': 'Program3 beskrivelse',
                'name': 'Program3',
                'posts': [
                ],
                'slug': 'program3',
                'updatedAt': '2018-03-23 21:29:54.395000+00:00'
            },
            {
                'archived': False,
                'categories': [
                ],
                'content': '<p>Program4 lenger beskrivelse!</p>',
                'createdAt': '2018-03-23 21:29:54.395000+00:00',
                'createdBy': {
                    'id': 2
                },
                'digasShowId': None,
                'episodes': [
                ],
                'id': 4,
                'image': '/media/uploads/images/300x300_9U7yu4U.png',
                'lead': 'Program4 beskrivelse',
                'name': 'Program4',
                'posts': [
                ],
                'slug': 'program4',
                'updatedAt': '2018-03-23 21:29:54.395000+00:00'
            }
        ]
    }
}

snapshots['test_show_by_id 1'] = {
    'data': {
        'show': {
            'archived': False,
            'categories': [
            ],
            'content': '<p>Program1 lenger beskrivelse</p>',
            'createdAt': '2018-02-23 21:29:09.247000+00:00',
            'createdBy': {
                'id': 2
            },
            'digasShowId': None,
            'episodes': [
                {
                    'id': 1
                }
            ],
            'id': 1,
            'image': '/media/uploads/images/300x300.png',
            'lead': 'Program1 beskrivelse',
            'name': 'Program1',
            'posts': [
            ],
            'slug': 'program1',
            'updatedAt': '2018-02-23 21:29:09.247000+00:00'
        }
    }
}

snapshots['test_all_episodes_with_offset 1'] = {
    'data': {
        'allEpisodes': [
            {
                'categories': [
                    {
                        'id': 1
                    }
                ],
                'createdAt': '2018-02-23 21:30:49.252000+00:00',
                'createdBy': {
                    'id': 2
                },
                'digasBroadcastId': None,
                'digasShowId': None,
                'id': 1,
                'lead': 'Dette er en episode',
                'onDemandUrl': 'http://example.com/lyd.mp3',
                'podcastUrl': None,
                'publishAt': '2018-02-23 21:30:14+00:00',
                'show': {
                    'id': 1
                },
                'title': 'Program1 23.02.2018',
                'updatedAt': '2018-02-23 21:30:49.252000+00:00'
            }
        ]
    }
}

snapshots['test_all_episodes 1'] = {
    'data': {
        'allEpisodes': [
            {
                'categories': [
                ],
                'createdAt': '2018-02-23 21:31:21.817000+00:00',
                'createdBy': {
                    'id': 2
                },
                'digasBroadcastId': None,
                'digasShowId': None,
                'id': 2,
                'lead': 'Beskrivelse av episode2',
                'onDemandUrl': 'http://example.com/lyd.mp3',
                'podcastUrl': None,
                'publishAt': '2018-02-23 21:30:51+00:00',
                'show': {
                    'id': 2
                },
                'title': 'Episode2',
                'updatedAt': '2018-02-23 21:31:21.817000+00:00'
            },
            {
                'categories': [
                    {
                        'id': 1
                    }
                ],
                'createdAt': '2018-02-23 21:30:49.252000+00:00',
                'createdBy': {
                    'id': 2
                },
                'digasBroadcastId': None,
                'digasShowId': None,
                'id': 1,
                'lead': 'Dette er en episode',
                'onDemandUrl': 'http://example.com/lyd.mp3',
                'podcastUrl': None,
                'publishAt': '2018-02-23 21:30:14+00:00',
                'show': {
                    'id': 1
                },
                'title': 'Program1 23.02.2018',
                'updatedAt': '2018-02-23 21:30:49.252000+00:00'
            }
        ]
    }
}

snapshots['test_all_episodes_with_count 1'] = {
    'data': {
        'allEpisodes': [
            {
                'categories': [
                    {
                        'id': 1
                    }
                ],
                'createdAt': '2018-02-23 21:30:49.252000+00:00',
                'createdBy': {
                    'id': 2
                },
                'digasBroadcastId': None,
                'digasShowId': None,
                'id': 1,
                'lead': 'Dette er en episode',
                'onDemandUrl': 'http://example.com/lyd.mp3',
                'podcastUrl': None,
                'publishAt': '2018-02-23 21:30:14+00:00',
                'show': {
                    'id': 1
                },
                'title': 'Program1 23.02.2018',
                'updatedAt': '2018-02-23 21:30:49.252000+00:00'
            }
        ]
    }
}

snapshots['test_post_by_id 1'] = {
    'data': {
        'post': {
            'categories': [
                {
                    'id': 1
                }
            ],
            'content': '<p>Enda mer tekst!</p>',
            'createdBy': {
                'id': 2
            },
            'croppedImages': {
                'large': '/media/cache/bf/0c/bf0c64d01f8854de77f44e8995bb6263.jpg',
                'medium': '/media/cache/b3/9c/b39c21c911d5cbfe60192fe818985a7e.jpg',
                'small': '/media/cache/8f/11/8f11ece1c53c8e55aadaa2cd700edcda.jpg',
                'thumbnail': '/media/cache/22/27/2227ce4a143ba45f0118c163462ef7a4.jpg'
            },
            'deleted': False,
            'episodes': [
            ],
            'id': 2,
            'image': 'uploads/images/700x350_HYkE6k8.png',
            'lead': 'Enda en ingress',
            'publishAt': '2018-02-23 21:30:30+00:00',
            'show': {
                'id': 2
            },
            'slug': 'den-andre-artikkelen',
            'title': 'Den andre artikkelen'
        }
    }
}

snapshots['test_all_posts 1'] = {
    'data': {
        'allPosts': [
            {
                'categories': [
                    {
                        'id': 1
                    }
                ],
                'content': '<p><b>Her</b> har vi teksten!</p>',
                'createdBy': {
                    'id': 2
                },
                'croppedImages': {
                    'large': '/media/cache/9c/7e/9c7ec938cac65a0bac80a67542ccf3af.jpg',
                    'medium': '/media/cache/0d/c6/0dc6a4cee46602608c70347932545628.jpg',
                    'small': '/media/cache/00/f2/00f21860fb35fef4b16ed402b407f846.jpg',
                    'thumbnail': '/media/cache/8e/8f/8e8fdbe3d759e3591c21d7d73effe9b6.jpg'
                },
                'deleted': False,
                'episodes': [
                    {
                        'id': 1
                    }
                ],
                'id': 1,
                'image': 'uploads/images/700x350.png',
                'lead': 'Ingressen her',
                'publishAt': '2018-02-23 21:31:29+00:00',
                'show': None,
                'slug': 'den-forste-artikkelen',
                'title': 'Den første artikkelen'
            },
            {
                'categories': [
                    {
                        'id': 1
                    }
                ],
                'content': '<p>Enda mer tekst!</p>',
                'createdBy': {
                    'id': 2
                },
                'croppedImages': {
                    'large': '/media/cache/bf/0c/bf0c64d01f8854de77f44e8995bb6263.jpg',
                    'medium': '/media/cache/b3/9c/b39c21c911d5cbfe60192fe818985a7e.jpg',
                    'small': '/media/cache/8f/11/8f11ece1c53c8e55aadaa2cd700edcda.jpg',
                    'thumbnail': '/media/cache/22/27/2227ce4a143ba45f0118c163462ef7a4.jpg'
                },
                'deleted': False,
                'episodes': [
                ],
                'id': 2,
                'image': 'uploads/images/700x350_HYkE6k8.png',
                'lead': 'Enda en ingress',
                'publishAt': '2018-02-23 21:30:30+00:00',
                'show': {
                    'id': 2
                },
                'slug': 'den-andre-artikkelen',
                'title': 'Den andre artikkelen'
            },
            {
                'categories': [
                    {
                        'id': 1
                    }
                ],
                'content': '<p><b>Her</b> har vi teksten!</p>',
                'createdBy': {
                    'id': 2
                },
                'croppedImages': {
                    'large': '/media/cache/9c/7e/9c7ec938cac65a0bac80a67542ccf3af.jpg',
                    'medium': '/media/cache/0d/c6/0dc6a4cee46602608c70347932545628.jpg',
                    'small': '/media/cache/00/f2/00f21860fb35fef4b16ed402b407f846.jpg',
                    'thumbnail': '/media/cache/8e/8f/8e8fdbe3d759e3591c21d7d73effe9b6.jpg'
                },
                'deleted': False,
                'episodes': [
                ],
                'id': 3,
                'image': 'uploads/images/700x350.png',
                'lead': 'Ingressen her',
                'publishAt': '2018-02-23 21:29:29+00:00',
                'show': None,
                'slug': 'den-3rd-artikkelen',
                'title': 'Den tredje artikkelen'
            },
            {
                'categories': [
                    {
                        'id': 1
                    }
                ],
                'content': '<p><b>Her</b> har vi teksten!</p>',
                'createdBy': {
                    'id': 2
                },
                'croppedImages': {
                    'large': '/media/cache/9c/7e/9c7ec938cac65a0bac80a67542ccf3af.jpg',
                    'medium': '/media/cache/0d/c6/0dc6a4cee46602608c70347932545628.jpg',
                    'small': '/media/cache/00/f2/00f21860fb35fef4b16ed402b407f846.jpg',
                    'thumbnail': '/media/cache/8e/8f/8e8fdbe3d759e3591c21d7d73effe9b6.jpg'
                },
                'deleted': False,
                'episodes': [
                ],
                'id': 7,
                'image': 'uploads/images/700x350.png',
                'lead': 'Ingressen her',
                'publishAt': '2018-02-23 21:25:29+00:00',
                'show': None,
                'slug': 'den-7th-artikkelen',
                'title': 'Den syvende artikkelen'
            }
        ]
    }
}

snapshots['test_all_posts_with_offset 1'] = {
    'data': {
        'allPosts': [
            {
                'categories': [
                    {
                        'id': 1
                    }
                ],
                'content': '<p><b>Her</b> har vi teksten!</p>',
                'createdBy': {
                    'id': 2
                },
                'croppedImages': {
                    'large': '/media/cache/9c/7e/9c7ec938cac65a0bac80a67542ccf3af.jpg',
                    'medium': '/media/cache/0d/c6/0dc6a4cee46602608c70347932545628.jpg',
                    'small': '/media/cache/00/f2/00f21860fb35fef4b16ed402b407f846.jpg',
                    'thumbnail': '/media/cache/8e/8f/8e8fdbe3d759e3591c21d7d73effe9b6.jpg'
                },
                'deleted': False,
                'episodes': [
                ],
                'id': 7,
                'image': 'uploads/images/700x350.png',
                'lead': 'Ingressen her',
                'publishAt': '2018-02-23 21:25:29+00:00',
                'show': None,
                'slug': 'den-7th-artikkelen',
                'title': 'Den syvende artikkelen'
            }
        ]
    }
}

snapshots['test_all_posts_with_count 1'] = {
    'data': {
        'allPosts': [
            {
                'categories': [
                    {
                        'id': 1
                    }
                ],
                'content': '<p><b>Her</b> har vi teksten!</p>',
                'createdBy': {
                    'id': 2
                },
                'croppedImages': {
                    'large': '/media/cache/9c/7e/9c7ec938cac65a0bac80a67542ccf3af.jpg',
                    'medium': '/media/cache/0d/c6/0dc6a4cee46602608c70347932545628.jpg',
                    'small': '/media/cache/00/f2/00f21860fb35fef4b16ed402b407f846.jpg',
                    'thumbnail': '/media/cache/8e/8f/8e8fdbe3d759e3591c21d7d73effe9b6.jpg'
                },
                'deleted': False,
                'episodes': [
                ],
                'id': 7,
                'image': 'uploads/images/700x350.png',
                'lead': 'Ingressen her',
                'publishAt': '2018-02-23 21:25:29+00:00',
                'show': None,
                'slug': 'den-7th-artikkelen',
                'title': 'Den syvende artikkelen'
            }
        ]
    }
}

snapshots['test_user_by_id 1'] = {
    'data': {
        'user': {
            'fullName': '',
            'id': 1,
            'publications': [
            ]
        }
    }
}

snapshots['test_all_users 1'] = {
    'data': {
        'allUsers': [
            {
                'fullName': '',
                'id': 1,
                'publications': [
                ]
            },
            {
                'fullName': 'Peder Ås',
                'id': 2,
                'publications': [
                    {
                        'id': 1
                    },
                    {
                        'id': 2
                    },
                    {
                        'id': 3
                    },
                    {
                        'id': 7
                    }
                ]
            }
        ]
    }
}
