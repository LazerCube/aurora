from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from authentication.permissions import is_owner

from authentication.models import Account

@login_required
def profile(request, username):
    profile = get_object_or_404(Account, username=username)
    has_permission = is_owner(request, profile)
    context = {
        'user': profile,
        'has_permission' : has_permission,
    }

    return render(request, 'user_profiles/user_profile.html', context)
