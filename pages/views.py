from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import Contact

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html' , {
        'linkedin_url': 'https://www.linkedin.com/in/mohammed-musthafa-v-469157274/'
    })
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        if name and email and subject and message:
            # Save to database
            Contact.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            # Try to send email, but don't fail if not configured
            try:
                full_subject = f'Contact from {name}: {subject}'
                full_message = f'Name: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}'
                send_mail(
                    full_subject,
                    full_message,
                    email,
                    ['musthafa6750@gmail.com'],
                    fail_silently=False,
                )
            except:
                pass  # Email failed, but submission saved
            messages.success(request, 'Your message has been sent! Thanks for reaching out.')
            return redirect('contact')
    return render(request, 'pages/contact.html')

def resume(request):
    return render(request, 'pages/resume.html')

def projects(request):
    return render(request, 'pages/projects.html')

def photos(request):
    return render(request, 'pages/photos.html')


