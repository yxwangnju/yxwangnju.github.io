#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

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

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True