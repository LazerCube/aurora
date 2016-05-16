from __future__ import unicode_literals
from news_feed.signals import action
from django.apps import AppConfig


class NewsFeedConfig(AppConfig):
    name = 'news_feed'

    def ready(self):
        from news_feed.actions import action_handler
        action.connect(action_handler)
