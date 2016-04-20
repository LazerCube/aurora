from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import json

def test_ajax(request):
    if request.method == 'POST':
        post_test = request.POST.get('test')
        response_data = {}

        response_data['message'] = 'Some error message'
        response_data['result'] = 'Success!'

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponseForbidden()

def login(request):
    if request.method =='POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/home')

        else:
            print("Failed")
            return HttpResponseRedirect('/')

    else:
        return HttpResponseForbidden()

def home(request):
    return render(request, 'index/index.html', {})

def index(request):
    return render(request, 'index/index.html', {})
