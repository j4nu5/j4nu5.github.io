#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Kushagra Sinha'
SITENAME = u'The Janus List'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (
    ('MobStac', 'http://www.mobstac.com/'),
    ("MobStac's blog", 'http://blog.mobstac.com/'),
)

# Social widget
SOCIAL = (
    ('Twitter', 'https://twitter.com/j4nu5'),
    ('LinkedIn', 'https://www.linkedin.com/in/sinhakushagra'),
    ('GitHub', 'https://github.com/j4nu5/'),
    ('Google+', 'https://plus.google.com/+KushagraSinha/'),
)

STATIC_PATHS = ['images', 'extra']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/README.md': {'path': 'README.md'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
}

DEFAULT_PAGINATION = 5

PYGMENTS_RST_OPTIONS = {'linenos': 'table'}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "pelican-sober"

PELICAN_SOBER_ABOUT = "Kushagra Sinha. Software Engineer at MobStac. Love python, distributed systems, reading and sleeping."
PELICAN_SOBER_STICKY_SIDEBAR = True

TYPOGRIFY = True

PLUGIN_PATHS = ["/Users/j4nu5/pelican-plugins"]
PLUGINS = ["sitemap"]

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
