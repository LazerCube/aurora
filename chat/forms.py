from django import forms
from friends.models import Friend

class CreateNewChatRoom(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'id' : 'inputChatName',
                                                        'class' : 'form-input',
                                                        'placeholder' : 'Name of Room',
                                                        'autocomplete' : 'off'}),
                                                        max_length=64)

    description = forms.CharField(widget=forms.Textarea(attrs={'id' : 'inputChatDesc',
                                                             'class' : 'form-input',
                                                             'placeholder' : 'Chat Room Description',
                                                             'autocomplete' : 'off'}),
                                                              max_length=128)

class CreateMessage(forms.Form):
    message = forms.CharField(widget=forms.Textarea(attrs={'id' : 'inputMessage',
                                                            'class' : 'form-input',
                                                            'placeholder' : 'Message',
                                                            'autocomplete' : 'off'}),
                                                            max_length=512)
