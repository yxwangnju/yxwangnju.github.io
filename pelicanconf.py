#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

THEME = "../themes/buruma"
AUTHOR = 'Audrey Wang'
SITENAME = '学习笔记 Tech Notebook'
SITEURL = ''

STATIC_PATHS = ['pictures']

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'en'

DEFAULT_DATE = 'fs'
DATE_FORMATS = {
    'en': '%a, %d %b %Y',
    'cn': '%Y-%m-%d(%a)',
}


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
# TAG_URL = 'tags.html'
# TAG_SAVE_AS = 'tags.html'

# Blogroll
LINKS = (('My GitHub Page', 'https://github.com/yxwangnju'),
         ('My Medium Blogs', 'https://audreywongkg.medium.com/'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com'),)

MENUITEMS_NAVBAR = (("About", "/pages/about.html"), 
                    ("How to set this page", "/pages/how-to-set-github-page.html"))

MENUITEMS_NAVBAR_FEATURED = (("Tags", "/tags.html", "is-link"),
                             ("Archives", "/archives.html", "is-link"))

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGIN_PATHS = ['../pelican-plugins', ]
PLUGINS = ['i18n_subsites', ]
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

IMAGE_PROCESS = {
    "crisp": {
        "type": "responsive-image",
        "srcset": [
            ("1x", ["scale_in 800 600 True"]),
            ("2x", ["scale_in 1600 1200 True"]),
            ("4x", ["scale_in 3200 2400 True"]),
        ],
        "default": "1x",
    },
    "large-photo": {
        "type": "responsive-image",
        "sizes": (
            "(min-width: 1200px) 800px, "
            "(min-width: 992px) 650px, "
            "(min-width: 768px) 718px, "
            "100vw"
        ),
        "srcset": [
            ("400w", ["scale_in 400 300 True"]),
            ("600w", ["scale_in 600 450 True"]),
            ("800w", ["scale_in 800 600 True"]),
            ("1600w", ["scale_in 1600 1200 True"]),
        ],
        "default": "400px",
    },
}
