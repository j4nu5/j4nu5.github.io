#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Kushagra Sinha'
SITENAME = u'The Janus List'
SITETITLE = u'The Janus List'
SITEDESCRIPTION = 'Personal blog of Kushagra Sinha'
SITEURL = ''
SITELOGO = SITEURL + '/images/pic.jpeg'

PATH = 'content'

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (
)

MENUITEMS = (
    ('Archives', '/archives.html'),
    ('Categories', '/categories.html'),
    ('Tags', '/tags.html'),
)

# Social widget
SOCIAL = (
    ('twitter', 'https://twitter.com/j4nu5'),
    ('linkedin', 'https://www.linkedin.com/in/sinhakushagra'),
    ('github', 'https://github.com/j4nu5/'),
    ('google', 'https://plus.google.com/+KushagraSinha/'),
    ('envelope-o', 'mailto:kush@j4nu5.com'),
    ('rss', '/feeds/all.atom.xml'),
)

STATIC_PATHS = ['images', 'extra']
ARTICLE_EXCLUDES = ['extra']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/README.md': {'path': 'README.md'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/googlea6407f1c0fbf99ee.html': {'path': 'googlea6407f1c0fbf99ee.html'},
}
READERS = {
    'html': None,
}

DEFAULT_PAGINATION = 5
MAIN_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True

PYGMENTS_RST_OPTIONS = {'linenos': 'table'}

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = "Flex"

USER_LOGO_URL = SITEURL + '/images/pic.jpeg'

TYPOGRIFY = True

PLUGIN_PATHS = ["/home/kushagra/workspace/pelican-plugins"]
PLUGINS = ["sitemap", "gist_directive"]

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'weekly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}
