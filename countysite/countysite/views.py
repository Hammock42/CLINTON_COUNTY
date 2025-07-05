from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from .forms import ContactForm



def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def coming_soon(request):
    return render(request, 'coming-soon.html')

def privacy_policy(request):
    return render(request, 'privacy-policy.html')

def legal_statement(request):
    return render(request, 'legal-statement.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            subject = form.cleaned_data.get('subject')
            message = form.cleaned_data.get('message')

            send_mail(
                subject,
                message,
                email,
                ["hamadhamdi13831@gmail.com"],
                fail_silently=False,
            )
            return render(request, 'contact.html', {'form': form, 'success': True})
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})