from __future__ import unicode_literals
from django.db import models

from authentication.models import Account
from embed_video.fields import EmbedVideoField

from chat.models import Room

POST_TYPE_CHOICES = (
    ('i','image'),
    ('v','video'),
    ('u', 'update'),
    ('t','text'),
    ('a','article')
)

class PostManager(models.Manager):
    def create_post(self, *args, **kwargs):
        if not 'type' in kwargs:
            kwargs['type'] = 'u'
        return self.model(*args, **kwargs)

    def video_post(self, video, **kwargs):
        return self.create_post(video=video, type='v', **kwargs)

class Posts(models.Model):
    author = models.ForeignKey(Account, editable=False)

    type = models.CharField(max_length=1, choices=POST_TYPE_CHOICES, db_index=True)

    message = models.TextField()
    video = EmbedVideoField(blank=True, null=True) #URL content to be embedded.
    likes = models.PositiveIntegerField(default=0)

    #picture =
    #link =

    public = models.BooleanField(default=True, db_index=True)
    created_at = models.DateTimeField(auto_now=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    objects = PostManager()

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __unicode__(self):
        if self.type == 'u':
            return 'status update'
        elif self.type == 'v':
            return 'video post'
        elif self.type == 'i':
            return 'image post'
        else:
            return self.message

    def comments(self):
        return Room.objects.get_for_object(self)

    def delete(self, *args, **kwargs):
        comments = self.comments()
        comments.delete()
        super(Posts, self).delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        super(Posts, self).save(*args, **kwargs)
