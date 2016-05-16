from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

from authentication.models import Account
from models import Activity

def feed(request):

    feed = Activity.objects.all()

    context = {
        'feed': feed,
    }

    return render(request, 'news_feed/feed.html', context)
