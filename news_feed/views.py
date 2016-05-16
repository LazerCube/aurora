from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

from authentication.models import Account
from activity.models import Activity
from models import Posts

from forms import StatusPostForm


@login_required
def home(request):
    form = StatusPostForm()
    if request.method == 'POST':
        form = StatusPostForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            Posts.object.create_post(author=request.user, message=message)
            return redirect('news_feed:index')

    context = {
        'form': form,
    }

    return render(request, 'news_feed/home.html', context)

@login_required
def feed(request):

    #feed = Activity.objects.actor(request.user)
    #feed = Activity.objects.public()
    feed = Activity.objects.user(request.user, with_user_activity=True)

    print(feed)

    context = {
        'feed': feed,
    }

    return render(request, 'news_feed/feed.html', context)
