from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def project(request):
    return render(request, 'projects.html')

def links(request):
    return render(request, 'links.html')
