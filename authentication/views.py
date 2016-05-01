from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.template import RequestContext #?????

from models import Account
from forms import LoginForm, RegisterForm


def register(request):
    if not request.user.is_authenticated():
        form = RegisterForm()
        email = ''
        first_name = ''
        last_name = ''
        username = ''
        password = ''

        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']

                account = Account.objects.create_user(email, password, username=username, first_name=first_name, last_name=last_name)

                return redirect('authenticate:login')


        context = RequestContext(request, {
                'first_name': first_name,
                'last_name': last_name,
                'form': form,
                'title':'Register',
        })
        return render(request, 'authentication/login/register.html', context)
    else:
        return redirect('user_profile', request.user.username)

def login(request):
    if not request.user.is_authenticated():
        form = LoginForm()
        username = ''
        password = ''
        state = ''
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)

                if user is not None:
                    if user.is_active:
                        auth_login(request, user)
                        print("Logged in")
                        return redirect('user_profile', request.user.username)
                    else:
                        state = "Your account is not active, please contact the administrator."

                else:
                    state = "Your username and/or password were incorrect."

        context = RequestContext(request, {
                'state': state,
                'username': username,
                'form': form,
                'title':'Login',
        })

        return render(request, 'authentication/login/login.html', context)
    else:
        return redirect('user_profile', request.user.username)

def logout(request):
    auth_logout(request)
    return redirect('/')
