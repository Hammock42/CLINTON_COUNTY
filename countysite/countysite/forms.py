from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"placeholder": "Your Name"}), required=True, label='Your Name')
    email = forms.EmailField(widget=forms.TextInput(attrs={"placeholder": "Your Email"}), required=True, label='Your Email')
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"placeholder": "Subject"}), required=True, label='Subject')
    message = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Your message"}), required=True, label='Message')