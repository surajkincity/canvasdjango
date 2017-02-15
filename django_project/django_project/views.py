from django.shortcuts import render
from django.http import HttpResponse
from django.templatetags.static import static



def home(request):
    return render(request, 'index.html', )
