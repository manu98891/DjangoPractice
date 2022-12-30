# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>Hola todo piola</h1>")

def hello(request,user):
    return HttpResponse("<h1> Hello world and hello %s </h1>" % user)

def about(request):
    return HttpResponse('Segundo mensaje')

def projects(request):
    return HttpResponse('projects')

def task(request):
    return HttpResponse('task')