from django.shortcuts import render
from .forms import *

# Create your views here.

def home(request, *args, **kwargs):
    data = Testimonial.objects.all()
    return render(request, 'home.html', {'data': data})


def contact(request, *args, **kwargs):
    form = CommentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            print(form)
            form.save()
    return render(request, 'contact-us.html', {})


def about(request, *args, **kwargs):
    return render(request, 'about-us.html', {})


def services(request, *args, **kwargs):
    return render(request, 'our-services.html', {})
