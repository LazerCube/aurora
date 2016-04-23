from django import forms
from django.forms.utils import ErrorList

class DivErrorList(ErrorList):
    def __unicode__(self):
        return self.as_divs()
    def as_divs(self):
        if not self: return ''
        return '<div class="errorlist">%s</div>' % ''.join(['<div class="error">%s</div>' % e for e in self])

class NameForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'id' : 'inputUsername',
                                                             'class' : 'form-input',
                                                             'placeholder' : 'Username',
                                                             'autocomplete' : 'off'}),
                                                             max_length=100)
    password= forms.CharField(widget=forms.PasswordInput(attrs={'id' : 'inputPassword',
                                                             'class' : 'form-input',
                                                             'placeholder' : 'Password'}))
