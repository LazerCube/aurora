from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.db.models import Q

from django.core.exceptions import ValidationError
from friends.exceptions import AlreadyExistsError, AlreadyFriendsError

from authentication.models import Account

class FriendManager(models.Manager):

    def friends(self, account):
        qs = Friend.objects.select_related('from_user', 'to_user').filter(to_user=account).all()
        friends = [u.from_user for u in qs]

        return friends

    def requests(self, account):
        requests = FriendRequest.objects.filter(from_user= account)
        qs = FriendRequest.objects.select_related('from_user', 'to_user').filter(
            to_user=account).all()
        requests = list(requests | qs)

        return requests

    def add_friend(self, from_user, to_user, message=None):
        if from_user == to_user:
            raise ValidationError("Users cannot be friends with themselves")

        if self.are_friends(from_user, to_user):
            raise AlreadyFriendsError("Users are already friends")

        if message is None:
            message = ''

        request, created = FriendRequest.objects.get_or_create(
            from_user=from_user,
            to_user=to_user,
        )

        if created is False:
            raise AlreadyExistsError("Friendship already requested")

        if message:
            request.message = message
            request.save()

        return request

    def remove_friend(self, to_user, from_user):
        try:
            qs = Friend.objects.filter(
                Q(to_user=to_user, from_user=from_user) |
                Q(to_user=from_user, from_user=to_user)
            ).distinct().all()

            print(qs)

            if qs:
                qs.delete()
                return True
            else:
                return False

        except Friend.DoesNotExist:
            return False

    def are_friends(self, user1, user2):
        try:
            Friend.objects.get(to_user=user2, from_user=user1)
            return True
        except Friend.DoesNotExist:
            return False


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
        return "Request ID:%s (User ID:%s friend request for ID:%s)" % (self.pk ,self.from_user.pk, self.to_user.pk)

    def cancel(self):
        self.delete()

        FriendRequest.objects.filter(
            from_user=self.to_user,
            to_user=self.from_user
        ).delete()

        return True

    def accept(self):
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
        if self.to_user == self.from_user:
            raise ValidationError("Users cannot be friends with themselves.")
        super(Friend, self).save(*args, **kwargs)
