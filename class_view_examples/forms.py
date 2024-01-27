from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(initial="Ivan")
    message = forms.CharField(widget=forms.Textarea, initial="Ivan message")
