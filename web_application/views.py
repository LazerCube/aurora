from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

from authentication.models import Account
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse

from authentication.permissions import is_owner

def profile(request, username):
    profile = get_object_or_404(Account, username=username)
    has_permission = is_owner(request, profile)
    context = {
        'user': profile,
        'has_permission' : has_permission,
    }

    return render(request, 'profiles/user_profile.html', context)

def index(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('user_profile', args=(request.user.username,)))
    return HttpResponseRedirect(reverse('authentication:login'))
