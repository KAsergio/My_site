from django import forms

class ContactForm(forms.Form):
    # https://docs.djangoproject.com/en/3.1/ref/forms/fields
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    phone = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)