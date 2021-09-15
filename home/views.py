from django.shortcuts import render

# Create your views here.

def home(request, *args, **kwargs):
    return render(request, 'home.html', {})


def contact(request, *args, **kwargs):
    return render(request, 'contact-us.html', {})


def about(request, *args, **kwargs):
    return render(request, 'about-us.html', {})


def services(request, *args, **kwargs):
    return render(request, 'our-services.html', {})
