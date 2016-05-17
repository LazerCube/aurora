from django import forms
from news_feed.models import Posts

from embed_video.fields import EmbedVideoFormField

class StatusPostForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea(attrs={'id' : 'inputMessage',
                                                           'class' : 'form-input-2 form-input',
                                                           'placeholder' : "What's on your mind?",
                                                           'autocomplete' : 'off',
                                                           'cols':40 }),
                                                            max_length=512)

    video_url = EmbedVideoFormField(widget=forms.TextInput(attrs={'id' : 'inputURL',
                                                           'class' : 'form-input-2 form-input',
                                                           'placeholder' : "URL for any videos",
                                                           'autocomplete' : 'off'}),required = False)
