from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from .forms import LoginForm, RegisterForm

from authentication.models import Account
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse

from authentication.permissions import is_owner

def profile(request, slug):
    has_permission = is_owner(request, slug)

    profile = get_object_or_404(Account, username=slug)
    context = {
        'user': profile,
        'has_permission' : has_permission,
    }

    return render(request, 'profiles/user_profile.html', context)


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

                return HttpResponseRedirect(reverse('login'))


        context = RequestContext(request, {
                'first_name': first_name,
                'last_name': last_name,
                'form': form,
                'title':'Register',
        })
        return render(request, 'web_application/login/register.html', {}, context)
    else:
        return HttpResponseRedirect(reverse('user_profile', args=(request.user.username,)))

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
                        return HttpResponseRedirect(reverse('user_profile', args=(request.user.username,)))
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

        return render(request, 'web_application/login/login.html', {}, context)
    else:
        return HttpResponseRedirect(reverse('user_profile', args=(request.user.username,)))

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/')

def index(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('user_profile', args=(request.user.username,)))
    return HttpResponseRedirect(reverse('login'))
