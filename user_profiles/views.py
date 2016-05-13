from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from authentication.permissions import is_owner
from django.db.models import Q

from friends.models import Friend
from authentication.models import Account

@login_required
def profile(request, username):
    profile = get_object_or_404(Account, username=username)

    are_friends = False
    has_permission = False

    has_permission = is_owner(request, profile)

    if is_owner(request, profile):
        has_permission = True
    else:
        are_friends = Friend.objects.are_friends(request.user, profile)


    context = {
        'user': profile,
        'are_friends': are_friends,
        'has_permission' : has_permission,
    }

    return render(request, 'user_profiles/user_profile.html', context)

@login_required
def search(request):
    results = None
    if request.method == 'GET':
        search_qry = request.GET.get('search_qry','')
        if not search_qry == '':
            results = Account.objects.find_users_by_name(search_qry)
        else:
            pass

    content = {
            'results' : results,
    }

    return render(request, 'user_profiles/search.html', content)
