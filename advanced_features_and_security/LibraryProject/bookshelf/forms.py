from django import forms

class ExampleForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100, required=True)
    description = forms.CharField(label='Description', widget=forms.Textarea, required=False)
    published_date = forms.DateField(label='Published Date', required=False)
