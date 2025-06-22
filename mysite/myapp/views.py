# from django.shortcuts import render

# def home(request):
#     return render(request, 'myapp/home.html')


# # Create your views here.
# from django.http import HttpResponse

# def home(request):
#     return HttpResponse("Welcome to My Django App!")


# Form set kiya ha 
from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm
from django.conf import settings

def home(request):
    success = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            full_message = f"From: {name}\nEmail: {email}\nSubject: {subject}\n\nMessage:\n{message}"
            
            send_mail(
                subject or "New Contact Form Submission",
                full_message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.CONTACT_RECEIVER_EMAIL],  # Define in .env
                fail_silently=False,
            )
            success = True
    else:
        form = ContactForm()

    return render(request, 'myapp/home.html', {'form': form, 'success': success})
