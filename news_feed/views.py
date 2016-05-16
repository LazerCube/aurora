from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

from authentication.models import Account

def feed(request):
    context = {
    }

    return render(request, 'news_feed/feed.html', context)
