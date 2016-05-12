from django import forms


class SearchForm(forms.Form):

    search_qry = forms.CharField(widget=forms.TextInput(attrs={'id' : 'search',
                                                              'placeholder' : 'Search',
                                                              'autocomplete' : 'off'}),
                                                              max_length=128)
