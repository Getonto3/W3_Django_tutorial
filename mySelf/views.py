from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader 

def mySelf(request):
    return HttpResponse("You know what they say, you snoze you lose!And it looks like you snost and you lost.")

def mySelf(request):
    template =loader.get_template('first.html')
    return HttpResponse(template.render())

# Create your views here.
