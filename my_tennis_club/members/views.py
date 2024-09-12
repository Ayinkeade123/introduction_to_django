

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def members(request):
    return HttpResponse("Hello world!")
    
def myfirst_html(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())

def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())

