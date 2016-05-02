from __future__ import unicode_literals

from django.db import models
from authentication.models import Account

from django.db.models import Prefetch

class ChatManager(models.Manager):
    def rooms(self, user):
        rooms = Room.objects.filter(subscribers=user)

        #rooms = Room.subscribers.through.objects.select_related('account').all()

        # qs = Room.subscribers.through.objects.select_related('account').filter(account_id=user).all()
        # rooms = [u.account for u in qs]

        # rooms = Room.objects.prefetch_related('subscribers').filter(subscribers=user).all()
        for u in rooms:
            print("Room: ", u)

        return rooms

    def create_room(self, user, name, description=None):
        if name == None:
            raise ValueError("Rooms must have a name")

        request = Room.objects.create(
            name=name,
            description=description,
        )

        request.subscribers.add(user)
        request.save()

        return request

class Room(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(null=True, blank=True, max_length=128)
    subscribers = models.ManyToManyField(Account)

    objects = ChatManager()

    def __str__(self):
        return "Room ID:%d | Name:%s | Desc:%s" % (self.pk, self.name, self.description)


    def save(self, *args, **kwargs):
        super(Room, self).save(*args, **kwargs)

class Message(models.Model):
    from_user = models.ForeignKey(Account, related_name="message_sent")
    to_user = models.ForeignKey(Account, related_name="message_received",blank=True, null=True)
    room = models.ForeignKey(Room)
    content = models.CharField(max_length=5000)
    created = models.DateTimeField(auto_now_add=True, editable=False)
