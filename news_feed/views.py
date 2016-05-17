from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required

from authentication.models import Account
from activity.models import Activity
from models import Posts

from forms import StatusPostForm
from activity.signals import action

from chat.models import Room
from friends.models import Friend

from django.db.models import Q

@login_required
def home(request):
    form = StatusPostForm()
    friends = Friend.objects.friends(request.user)

    qs = Q()
    for friend in friends:
        qs = qs | Q(author=friend)
    qs = qs | Q(author=request.user)
    posts = Posts.objects.filter(qs).order_by('-created_at')

    if request.method == 'POST':
        form = StatusPostForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            video = form.cleaned_data['video_url']
            if video == '':
                post = Posts.objects.create_post(author=request.user, message=message)
            else:
                post = Posts.objects.video_post(video, author=request.user, message=message)

            post.save()
            Room.objects.get_or_create(post, name="post-comments", desc="post comments")
            #Room.objects.get_or_create(post)
            action.send(request.user, verb='posted', target=post)
            return redirect('news_feed:index')

    context = {
        'form': form,
        'posts': posts,
    }

    return render(request, 'news_feed/home.html', context)
