from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required

from authentication.models import Account

@login_required
def view_chatrooms(request):
    return render(request, 'chat/chat_rooms.html')
