from django import forms
from news_feed.models import Posts

class StatusPostForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea(attrs={'id' : 'inputMessage',
                                                           'class' : 'form-input-2 form-input',
                                                           'placeholder' : "What's on your mind?",
                                                           'autocomplete' : 'off',
                                                           'cols':40 }),
                                                            max_length=512)
