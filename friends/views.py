from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse

from authentication.models import Account
from models import Friend

def view_friends(request, username):
    """ View the friends of a user """
    user = get_object_or_404(Account, username=username)
    friends = Friend.objects.friends(user)
    return render(request, 'friends/friends.html', {'friends': friends})

@login_required
def view_requests(request, username):
    user = Account.objects.get(username=username)
    friends = Friend.objects.requests(user)

    return render(request, 'friends/requests.html', {'friends': friends})

@login_required
def add_friends(request, username):
    """ View the friends of a user """

    to_user = Account.objects.get(username=username)
    from_user = request.user
    print("---------------------")
    print("---------------------")
    print("From %s to %s" % (from_user, to_user))
    Friend.objects.add_friend(from_user, to_user)

    return redirect('index')
