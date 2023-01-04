# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404


# Create your views here.
def index(request):
    return HttpResponse("<h1>Hola todo piola</h1>")

def hello(request,user):
    return HttpResponse("<h1> Hello world and hello %s </h1>" % user)

def about(request):
    return HttpResponse('Segundo mensaje')

def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)

def task(request, id):
    #task = Task.objects.get(id=id)
    task = get_object_or_404(Task,id=id)
    return HttpResponse('task: %s' % task.title)