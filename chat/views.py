from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required

from authentication.models import Account
from models import Room

@login_required
def view_chatrooms(request):
    user = request.user
    rooms = Room.objects.rooms(user)

    return render(request, 'chat/chat_rooms.html', {'rooms': rooms})
