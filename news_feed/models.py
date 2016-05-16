from __future__ import unicode_literals
from django.db import models

from authentication.models import Account

POST_TYPE_CHOICES = (
    ('i','image'),
    ('v','video'),
    ('u', 'update'),
    ('t','text'),
    ('a','article')
)

class PostManager(models.Manager):
    # def create_post(self, type, author, message, **kwargs):
    #     '''Function for creating posts'''
    #     p = self.model(author=author, type=type, message=message)
    #     p.save()

    def create_post(self, *args, **kwargs):
        if not 'type' in kwargs:
            kwargs['type'] = 'u'
        p = self.model(*args, **kwargs)
        p.save()
        return p

    def video_post(self, url, **kwargs):
        return self.create_post(source=url, type='v')

class Posts(models.Model):
    author = models.ForeignKey(Account, editable=False)

    type = models.CharField(max_length=1, choices=POST_TYPE_CHOICES, db_index=True)

    message = models.TextField()
    source = models.URLField(blank=True, null=True) #URL content to be embedded.
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

    def save(self, *args, **kwargs):
        super(Posts, self).save(*args, **kwargs)
