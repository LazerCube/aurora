from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse

from authentication.permissions import is_owner

from authentication.models import Account
from models import Friend, FriendRequest

@login_required
def view_friends(request):
    """ View the friends of a user """
    user = request.user
    friends = Friend.objects.friends(user)
    return render(request, 'friends/friends.html', {'friends': friends})

@login_required
def view_requests(request):
    user = request.user
    friends = Friend.objects.requests(user)

    return render(request, 'friends/requests.html', {'friends': friends})

@login_required
def accept_friends(request, friendship_request_id):
    print("-----------------------------------------------------------")

    f_request = get_object_or_404(request.user.friend_requests_received,
        id=friendship_request_id)

    f_request.accept()

    return redirect('index')

@login_required
def add_friends(request, to_username):
    """ View the friends of a user """

    to_user = get_object_or_404(Account, username=to_username)
    from_user = request.user
    Friend.objects.add_friend(from_user, to_user)

    return redirect('index')
