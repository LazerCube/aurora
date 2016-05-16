from __future__ import unicode_literals
from django.utils.timesince import timesince as djtimesince
from django.db import models

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.

class ActivityManager(models.Manager):
    def public(self, *args, **kwargs):
        '''Returns public actions'''
        pass

VERB_TYPE_CHOICES = (
    ('add'),
    ('delete'),
    ('invite'),
    ('join'),
    ('leave'),
    ('like'),
    ('unlike'),
    ('request-friend'),
    ('remove-friend'),
    ('save'),
    ('update')
)

class Activity(models.Model):
    '''

        Generalized Format::
            <actor> <verb> <time>
            <actor> <verb> <target> <time>
            <actor> <verb> <action_object> <target> <time>
        Examples::
            <lazer> <Logged in> <1 minute ago>
            <lazer> <commented on> <lazer-snorlax> <2 hours ago>
            <snorlax> <started follow> <lazer> <8 minutes ago>
            <mitsuhiko> <deleted> <message 2> on <lazer-snorlax> <about 2 hours ago>

    '''
    actor_content_type = models.ForeignKey(ContentType, related_name='actor',
                                            db_index=True)
    actor_object_id = models.PositiveIntegerField(db_index=True)
    actor = GenericForeignKey('actor_content_type', 'actor_object_id') # who did it (what object)

    verb = models.CharField(max_length=255, db_index=True) # What did they do?
    description = models.TextField(blank=True, null=True)

    target_content_type = models.ForeignKey(ContentType, blank=True, null=True,
                                            related_name='target', db_index=True)

    target_object_id = models.PositiveIntegerField(blank=True, null=True, db_index=True)
    target = GenericForeignKey('target_content_type', 'target_object_id') #what did they do it on? (object eg chatroom)


    action_object_content_type = models.ForeignKey(ContentType, blank=True, null=True,
                                                   related_name='action_object', db_index=True)
    action_object_object_id = models.PositiveIntegerField(blank=True, null=True, db_index=True)
    action_object = GenericForeignKey('action_object_content_type','action_object_object_id') #What part did they do it on

    public = models.BooleanField(default=True, db_index=True) # can other people see it?
    timestamp = models.DateTimeField(auto_now=True, editable=False) # Time they did it at

    def __str__(self):
        ctx = {
            'actor': self.actor,
            'verb': self.verb,
            'action_object': self.action_object,
            'target': self.target,
            'timesince': self.timesince()
        }
        if self.target:
            if self.action_object:
                return ('%(actor)s %(verb)s %(action_object)s on %(target)s %(timesince)s ago') % ctx
            return ('%(actor)s %(verb)s %(target)s %(timesince)s ago') % ctx
        if self.action_object:
            return ('%(actor)s %(verb)s %(action_object)s %(timesince)s ago') % ctx
        return ('%(actor)s %(verb)s %(timesince)s ago') % ctx

    def timesince(self, now=None):
        return djtimesince(self.timestamp, now).encode('utf8').replace(b'\xc2\xa0', b' ').decode('utf8')
