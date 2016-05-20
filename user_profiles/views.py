from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from authentication.permissions import is_owner
from django.db.models import Q

from friends.models import Friend
from authentication.models import Account

from news_feed.forms import StatusPostForm
from activity.models import Activity

from authentication.forms import EditForm

@login_required
def profile(request, username):

    form = StatusPostForm()

    profile = get_object_or_404(Account, username=username)
    feed = Activity.objects.user(profile, with_user_activity=True).order_by('-timestamp')

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
        'feed': feed,
        'form': form,
    }

    return render(request, 'user_profiles/user_profile.html', context)

@login_required
def edit(request):
    form = EditForm()
    profile = get_object_or_404(Account, pk=request.user.pk)

    if request.method == 'POST':
        form = EditForm(request.POST, request.FILES)
        if form.is_valid():
            avatar = form.cleaned_data['avatar']
            profile.set_avatar(avatar)

            return redirect('user_profile:edit')

    context = {
        'user': profile,
        'form': form,
    }

    return render(request, 'user_profiles/edit.html', context)

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
