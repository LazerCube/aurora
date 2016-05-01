from django.shortcuts import render, redirect
from django.contrib.auth import authenticate

def index(request):
    if request.user.is_authenticated():
        return redirect('user_profile:index', request.user.username)
    return redirect('authentication:login')
