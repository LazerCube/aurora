from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required

from authentication.models import Account
from models import Room
from forms import CreateNewChatRoom

from django.template import RequestContext

@login_required
def view_chatrooms(request):
    name = ""
    description = ""

    rooms = Room.objects.rooms(request.user)
    form = CreateNewChatRoom()

    if request.method == 'POST':
        form = CreateNewChatRoom(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']

            # try:
            #     Room.objects.create_room(user, name, description)
            # except Exception as e:
            #     content['errors'] = ["%s" %(e)]
            # else:
            #     return redirect('chat:view_chatrooms')

            Room.objects.create_room(request.user, name, description)
            return redirect('chat:view_chatrooms')

    content = RequestContext(request, {
            'rooms': rooms,
            'form': form,
    })

    return render(request, 'chat/chat_rooms.html', content)

@login_required
def view_chat(request,chatroom_id):
    chatroom = get_object_or_404(Room, pk=chatroom_id)

    content = RequestContext(request, {
            'chatroom': chatroom,
    })

    return render(request, 'chat/conversation.html', content)
