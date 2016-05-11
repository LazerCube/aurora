from django.shortcuts import render, redirect
from django.contrib.auth import authenticate

def index(request):
    if request.user.is_authenticated():
        return redirect('user_profile:index', request.user.username)
    return redirect('authentication:login')

def test(request):
    return render(request, 'web_application/test.html')

def handler403(request):
    msg = "Forbidden."

    context = {
        'error_code': 403,
        'message': msg,
    }

    return render(request, 'web_application/errorhandler.html', context)

def handler404(request):
    msg = "We couldn't find the page you were looking for."

    context = {
        'error_code': 404,
        'message': msg,
    }

    return render(request, 'web_application/errorhandler.html', context)


def handler500(request):
    msg = "Server Error."

    context = {
        'error_code': 500,
        'message': msg,
    }

    return render(request, 'web_application/errorhandler.html', context)
