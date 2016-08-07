from django import forms
from . models import SimpleList

class SimpleListForm(forms.ModelForm):
    class Meta:
        model = SimpleList
        fields = ('shortname', 'contents')
        labels = {
                'shortname': (u'Name'),
                'contents': (u'List'),
        }

class loginForm(forms.Form):
    username=forms.CharField(max_length=200)
    password=forms.CharField(max_length=30)
