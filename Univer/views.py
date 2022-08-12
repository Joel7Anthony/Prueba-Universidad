from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm

# Create your views here.
def list_Uni(request):
    Univer = Task.objects.all()
    return render(request, 'list_Uni.html', {"Univer": Univer})

def create_task(request):
    task=Task(decano=request.POST['decano'], apellido=request.POST['apellido'], titulo=request.POST['titulo'], descripcion=request.POST['descripcion'], direccion=request.POST['direccion'])
    task.save()
    return redirect('/Univer/')

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect("/Univer/")

def editar_task(request,task_id):
   task = Task.objects.get(id=task_id)
   
   task.decano   = request.POST["decano"]
   task.apellido = request.POST["apellido"]
   task.titulo   = request.POST["titulo"]
   task.descripcion = request.POST["descripcion"]
   task.direccion = request.POST["direccion"]
   
   task.save()
   return redirect("/Univer/")
   