from django import forms
from authentication.models import Account

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
    class Meta:
        model = Account

    def clean_username(self):
        username = self.cleaned_data['username']
        if Account.objects.filter(username=username).exists():
            raise forms.ValidationError('The Username, %s is already in use.' % username)
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if Account.objects.filter(email=email).exists():
            raise forms.ValidationError('The Email, %s is already in use.' % email)
        return email

class EditForm(forms.Form):
    profile_picture = forms.ImageField()
