from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def resume(request):
    return render(request, 'pages/resume.html')

def projects(request):
    return render(request, 'pages/projects.html')

def contact(request):
    return render(request, 'pages/contact.html')

def photos(request):
    return render(request, 'pages/photos.html')
