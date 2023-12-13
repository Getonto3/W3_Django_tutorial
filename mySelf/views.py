from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader 
from .models import MySelf

# Create your views here.
def mySelf(request):
    return HttpResponse("You know what they say, you snoze you lose!And it looks like you snost and you lost.")

def mySelf(request):
    template =loader.get_template('first.html')
    return HttpResponse(template.render())

def members(request):
    members= MySelf.objects.all().values()
    template=loader.get_template('members.html')
    context ={
        'members':members,   
    }
    return HttpResponse(template.render(context, request))

def details(request,id):
    members=MySelf.objects.get(id=id)
    template=loader.get_template('details.html')
    context = {
        'members': members,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())
    
def first(request):
    template = loader.get_template('first.html')
    return HttpResponse(template.render())

def testing(request):
  mydata=MySelf.objects.values()
  template = loader.get_template('template.html')
  context = {
    'Members': mydata,
  }
  return HttpResponse(template.render(context, request))