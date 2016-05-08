from django.shortcuts import render, redirect
from django.contrib.auth import authenticate

def index(request):
    if request.user.is_authenticated():
        return redirect('user_profile:index', request.user.username)
    return redirect('authentication:login')

def handler404(request):
    msg = "Page Not Found."

    context = {
        'error_code': 404,
        'error': msg,
    }

    return render(request, 'web_application/errorhandler.html', context)


def handler500(request):
    msg = "Server Error."

    context = {
        'error_code': 500,
        'error': msg,
    }

    return render(request, 'web_application/errorhandler.html', context)
