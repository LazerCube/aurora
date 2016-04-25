from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from .forms import DivErrorList, LoginForm

from authentication.models import Account
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse

class UserProfileView(DetailView):
    model = Account
    slug_field = "username"
    template_name = "profiles/user_profile.html"
    title='User Profile'

def login(request):
    if not request.user.is_authenticated():
        form = LoginForm()
        username = ''
        password = ''
        state = ''
        if request.method == 'POST':
            form = LoginForm(request.POST, error_class=DivErrorList)
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
    return render(request, 'web_application/index/index.html', {})
