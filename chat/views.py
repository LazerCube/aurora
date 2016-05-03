from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required

from authentication.models import Account
from chat.models import Room, Message
from forms import CreateNewChatRoom, CreateMessage

from django.template import RequestContext

@login_required
def view_chatrooms(request):
    name = ""
    description = ""

    rooms = Room.objects.all()
    form = CreateNewChatRoom()

    if request.method == 'POST':
        form = CreateNewChatRoom(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']

            u = request.user
            r = Room.objects.get_or_create(u, name, description)

            return redirect('chat:view_chatrooms')

    content = RequestContext(request, {
            'rooms': rooms,
            'form': form,
    })

    return render(request, 'chat/chat_rooms.html', content)

@login_required
def view_chat(request,chatroom_id):
    r = get_object_or_404(Room, pk=chatroom_id)
    m = r.messages()
    f = CreateMessage()

    print(m)

    if request.method == 'POST':
        f = CreateMessage(request.POST)
        if f.is_valid():
            message = f.cleaned_data['message']
            r.say(request.user, message)
            print("MESSAGE SENT")

            return redirect('chat:view_chat', r.pk)

    content = {
            'chatroom': r,
            'messages': m,
            'form': f,
    }

    return render(request, 'chat/conversation.html', content)

@login_required
def send(request, chatroom_id):
    '''recives messages sent and links to corresponding room model'''




@login_required
def sync(requst):
    '''will get the last message sent to chat. so you can't see msg from before you joinned'''

@login_required
def receive(requst):
    '''called by the client javacript code, returns a list of messages sent'''

@login_required
def join(request):
    '''called when a user joins a chat room'''

@login_required
def leave(request):
    '''called when a user leaves a chat room'''
