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
                                                             'placeholder' : 'Email',
                                                             'autocomplete' : 'off'}),
                                                             max_length=100)
    password= forms.CharField(widget=forms.PasswordInput(attrs={'id' : 'inputPassword',
                                                             'class' : 'form-input',
                                                             'placeholder' : 'Password'}))
class RegisterForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'id' : 'inputEmail',
                                                             'class' : 'form-input',
                                                             'placeholder' : 'Email',
                                                             'autocomplete' : 'off'}),
                                                             max_length=100)

    username = forms.CharField(widget=forms.TextInput(attrs={'id' : 'inputUsername',
                                                             'class' : 'form-input',
                                                             'placeholder' : 'Username',
                                                             'autocomplete' : 'off'}),
                                                             max_length=100)

    first_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'inputFirstName',
                                                             'class' : 'form-input',
                                                             'placeholder' : 'Forename',
                                                             'autocomplete' : 'off'}),
                                                             max_length=100)

    last_name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'inputLastName',
                                                             'class' : 'form-input',
                                                             'placeholder' : 'Surname',
                                                             'autocomplete' : 'off'}),
                                                             max_length=100)

    password = forms.CharField(widget=forms.PasswordInput(attrs={'id' : 'inputPassword',
                                                             'class' : 'form-input',
                                                             'placeholder' : 'Password'}))

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.exclude(pk=self.instance.pk).filter(username=username).exists():
            raise forms.ValidationError(u'Username "%s" is already in use.' % username)
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.exclude(pk=self.instance.pk).filter(email=email).exists():
            raise forms.ValidationError(u'Email "%s" is already in use.' % email)
        return email
