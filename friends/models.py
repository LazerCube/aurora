from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

from authentication.models import Account

class FriendManager(models.Manager):
    """ Friendship manager """

    def friends(self, account):
        """ Return a list of all friends """
        friends = Friend.objects.filter(to_user= account)

        if not Friend.objects.filter(to_user= account).exists():
            qs = Friend.objects.select_related('from_user', 'to_user').filter(to_user=account).all()
            friends = [u.from_user for u in qs]

        return friends

    def requests(self, account):
        requests = FriendRequest.objects.filter(from_user= account)
        if not FriendRequest.objects.filter(from_user= account).exists():
            qs = FriendRequest.objects.select_related('from_user', 'to_user').filter(
                to_user=account).all()
            requests = list(qs)
        return requests

    def add_friend(self, from_user, to_user, message=None):
        """ sends a friend request """

        if from_user == to_user:
            raise ValidationError("Users cannot be friends with themselves")

        if message is None:
            message = ''

        request, created = FriendRequest.objects.get_or_create(
            from_user=from_user,
            to_user=to_user,
        )

        if message:
            request.message = message
            request.save()

        return request

    def are_friends(self, account1, account2):
        """ Checks if two users are friends """
        return false

@python_2_unicode_compatible
class FriendRequest(models.Model):
    from_user = models.ForeignKey(Account, related_name="friend_requests_sent")
    to_user = models.ForeignKey(Account, related_name="friend_requests_received")

    message = models.TextField(('Message'), blank=True)

    created = models.DateTimeField(auto_now_add=True, editable=False)
    rejected = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = ('Friendship Request')
        verbose_name_plural = ('Friendship Requests')
        unique_together = ('from_user', 'to_user')

    def __str__(self):
            return "User ID:%s friend request for ID:%s" % (self.from_user.pk, self.to_user.pk)

    def accept(self):
        print("--ACCEPT--")
        relation1 = Friend.objects.create(
            from_user=self.from_user,
            to_user=self.to_user
        )

        relation2 = Friend.objects.create(
            from_user=self.to_user,
            to_user=self.from_user
        )

        self.delete()

        # Delete any reverse requests
        FriendRequest.objects.filter(
            from_user=self.to_user,
            to_user=self.from_user
        ).delete()

        return True

    def decline(self):
        self.rejected = timezone.now()
        self.save()
        return True

@python_2_unicode_compatible
class Friend(models.Model):
    to_user = models.ForeignKey(Account, related_name='friends')
    from_user = models.ForeignKey(Account, related_name='_unused_friend_relation')
    created = models.DateTimeField(default=timezone.now)

    objects = FriendManager()

    class Meta:
        verbose_name = ('Friend')
        verbose_name_plural = ('Friends')
        unique_together = ('from_user', 'to_user')

    def __str__(self):
        return "User ID:%d is friends with ID:%d" % (self.to_user_id, self.from_user_id)

    def save(self, *args, **kwargs):
        """ Save Friends """
        if self.to_user == self.from_user:
            raise ValidationError("Users cannot be friends with themselves.")
        super(Friend, self).save(*args, **kwargs)
