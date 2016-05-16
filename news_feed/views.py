from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required

from authentication.models import Account
from activity.models import Activity
from models import Posts

from forms import StatusPostForm
from activity.signals import action

@login_required
def home(request):
    form = StatusPostForm()
    posts = Posts.objects.all()

    if request.method == 'POST':
        form = StatusPostForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            post = Posts.objects.create_post(author=request.user, message=message)
            action.send(request.user, verb='posted', target=post)
            return redirect('news_feed:index')

    context = {
        'form': form,
        'posts': posts,
    }

    return render(request, 'news_feed/home.html', context)
