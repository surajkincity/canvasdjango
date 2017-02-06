from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    this = 'this'
    return render(request, 'index.html', {'this': this})

def css(request):
    this = 'this'
    return render(request, 'main.css', {'this': this})
