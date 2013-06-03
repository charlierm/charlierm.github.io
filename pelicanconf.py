#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Charlie Mills'
SITENAME = u'Computerbacon'
SITEURL = ''

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

DATE_FORMAT = {
'en': '%d %m %Y'
}

STATIC_PATHS = ["images"]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Github', 'http://github.com/charlierm'),
          ('Twitter', 'http://twitter.com/charlesthe6th'),
          ('LinkedIn', 'http://uk.linkedin.com/in/computerbacon'),)

# Social widget
SOCIAL = (('Github', 'http://github.com/charlierm'),
          ('Twitter', 'http://twitter.com/charlesthe6th'),
          ('LinkedIn', 'http://uk.linkedin.com/in/computerbacon'),)


SECTIONS = [('Blog', 'index.html'),
        ('Archive', 'archives.html'),
        ('Tags', 'tags.html'),
        ('About', 'pages/about.html')]


MAIL_USERNAME = 'charlie'
MAIL_HOST = 'computerbacon.com'


DISQUS_SITENAME = "computerbacon"
TWITTER_USERNAME = 'charlesthe6th'
LINKEDIN_URL = 'http://uk.linkedin.com/in/computerbacon'
GITHUB_URL = 'http://github.com/charlierm'


GOOGLE_ANALYTICS_ACCOUNT = 'UA-41412641-1'
GOOGLE_ANALYTICS = 'UA-41412641-1'

PIWIK_URL = 'vps.computerbacon.com/piwik'
PIWIK_SSL_URL = 'vps.computerbacon.com/piwik'
PIWIK_SITE_ID = '1'


FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'


ARTICLE_URL = "posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/"
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'

DEFAULT_PAGINATION = 10

DEFAULT_CATEGORY = 'Uncategorized'

SUMMARY_MAX_LENGTH = None

PLUGIN_PATH = 'plugins/'

PLUGINS = ['sitemap']

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "theme/flasky"