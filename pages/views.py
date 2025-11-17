from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html' , {
        'linkedin_url': 'https://www.linkedin.com/in/mohammed-musthafa-v-469157274/'
    })

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully.')
            return redirect('contact')
        else:
            messages.error(request, 'There was an error submitting your message. Please check the form.')
    else:
        form = ContactForm()
    return render(request, 'pages/contact.html', {'form': form})
    
def resume(request):
    return render(request, 'pages/resume.html')

def projects(request):
    return render(request, 'pages/projects.html')

def documents(request):
    return render(request, 'pages/documents.html')


