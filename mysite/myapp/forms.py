from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Full Name")
    email = forms.EmailField(label="Email Address")
    subject = forms.CharField(max_length=150, required=False)
    message = forms.CharField(widget=forms.Textarea, label="Your Message")
