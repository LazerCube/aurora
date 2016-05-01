from __future__ import unicode_literals

from django.db import models
from authentication.models import Account


class ChatManager(models.Manager):
    def rooms(self, user):
        rooms = Room.objects.select_related('subscribers').filter(subscribers=user).all()
        return rooms


    def create_room(self, name, description=None):
        if name == none:
            raise ValueError("Rooms must have a name")

        user = self.request.user

        request = Room.objects.create(
            name=name,
            description=description,
            subscribers=user,
        )

        return request


class Room(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField()
    subscribers = models.ManyToManyField(Account, blank=True)

    objects = ChatManager()

    def save(self, *args, **kwargs):
        super(Room, self).save(*args, **kwargs)

class Message(models.Model):
    from_user = models.ForeignKey(Account, related_name="message_sent")
    to_user = models.ForeignKey(Account, related_name="message_received",blank=True, null=True)
    room = models.ForeignKey(Room)
    content = content = models.CharField(max_length=5000)
    created = models.DateTimeField(auto_now_add=True, editable=False)
