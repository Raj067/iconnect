from django.shortcuts import render

# Create your views here.

def home(request, *args, **kwargs):
    return render(request, 'home.html', {})


def contact(request, *args, **kwargs):
    return render(request, 'contact-us.html', {})
