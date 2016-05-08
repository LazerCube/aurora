from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required

from authentication.models import Account
from chat.models import Room, Message
from forms import CreateNewChatRoom, CreateMessage

from django.template import RequestContext

from django.http import HttpResponse
from django.template.loader import render_to_string
import json

from guardian.shortcuts import get_objects_for_user
from guardian.core import ObjectPermissionChecker

@login_required
def view_chatrooms(request):
    name = ""
    description = ""

    rooms = get_objects_for_user(request.user, 'chat.view_room')
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
    checker = ObjectPermissionChecker(request.user)
    if checker.has_perm('view_room', r):
        f = CreateMessage()

        content = {
                'chatroom': r,
                'form': f,
        }

        return render(request, 'chat/conversation.html', content)
    else:
        return redirect('chat:view_chatrooms')

@login_required
def send(request):
    '''recives messages sent and links to corresponding room model'''
    if request.method == 'POST':
        response_data = {}
        room_id = request.POST.get('room_id')
        message = request.POST.get('message')

        r = get_object_or_404(Room, pk=room_id)

        r.say(request.user, message)
        print("MESSAGE SENT")

        response_data['response'] = 'Create message successful!'

        return HttpResponse(
            json.dumps(response_data), content_type="application/json")

    else:
        return HttpResponse(
            json.dumps({ Error : "Something went wrong."}),
            content_type="application/json"
        )

@login_required
def sync(request):
    '''will get the last message sent to chat.'''
    if request.method == 'POST':
        response_data = {}
        room_id = request.POST.get('room_id')
        last_id = request.POST.get('last_id')

        r = get_object_or_404(Room, pk=room_id)
        m = r.messages(after_pk=last_id)

        content = {
            'messages': m,
            'request': request,
        }

        response_data = render_to_string('chat/includes/messages.html', content)
        return HttpResponse(response_data)

    else:
        return HttpResponse(
            json.dumps({ Error : "Something went wrong."}),
            content_type="application/json"
        )

@login_required
def receive(request):
    '''called by the client javacript code, returns a list of messages sent'''
    if request.method == 'POST':
        response_data = {}
        room_id = request.POST.get('room_id')

        r = get_object_or_404(Room, pk=room_id)
        m = r.messages()

        content = {
            'messages': m,
            'request': request,
        }

        response_data = render_to_string('chat/includes/messages.html', content)
        return HttpResponse(response_data)

    else:
        return HttpResponse(
            json.dumps({ Error : "Something went wrong."}),
            content_type="application/json"
        )

# @login_required
# def join(request):
#     '''called when a user joins a chat room'''
#
# @login_required
# def leave(request):
#     '''called when a user leaves a chat room'''
