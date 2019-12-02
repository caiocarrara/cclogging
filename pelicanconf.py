#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Caio Carrara'
AUTHOR_EMAIL = 'eu@caiocarrara.com.br'
SITENAME = 'cC Log'
SITEURL = 'http://localhost:8000'

TAGLINE = (
    'Caio Carrara, Programação, Python, Software, Liberdade e Autonomia'
)

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'pt_br'

USE_FOLDER_AS_CATEGORY = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DELETE_OUTPUT_DIRECTORY = True  # on each site generation

THEME = 'themes/cclogging'

ARTICLE_PATHS = ['posts']
ARTICLE_URL = ARTICLE_SAVE_AS = 'blog/{slug}.html'
PAGE_URL = PAGE_SAVE_AS = '{slug}.html'
TAG_URL = TAG_SAVE_AS = 'tags/{slug}.html'
DIRECT_TEMPLATES = ['index', 'blog']
PAGINATED_TEMPLATES = {'blog': None}

SLUGIFY_SOURCE = 'title'

NEWEST_FIRST_ARCHIVES = True

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
    ('github', 'https://github.com/cacarrara/'),
    ('twitter', 'https://twitter.com/CaioWCC'),
    ('rss', 'http://caiocarrara.com.br/feeds/caio-carrara.atom.xml'),
)

DEFAULT_PAGINATION = 7

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
