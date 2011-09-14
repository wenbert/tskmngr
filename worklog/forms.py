from django import forms

class CreateWorklogForm(forms.Form):
   title = forms.CharField(label = 'Title of your Worklog',required=True)
   desc = forms.CharField(label = 'Enter a description', required=False, \
          widget=forms.Textarea)
