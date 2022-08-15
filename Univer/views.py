from django.shortcuts import render,redirect
from .models import Task


# Create your views here.
def list_Uni(request):
    task = Task.objects.all()
    context = {
        "task": task[::-1],
        "update_from": None
    }
    return render(request, 'list_Uni.html', context)

def insert(request):
    try:
        task_decano = request.POST['decano']
        task_apellido = request.POST['apellido']
        task_titulo = request.POST['titulo']
        task_descripcion = request.POST['descripcion']
        task_direccion = request.POST['direccion']
        if task_decano == "" or task_apellido == "" or task_titulo == "" or task_descripcion == "" or task_descripcion == "":
            raise ValueError("El texto no puede estar vacio.")
        task = Task(decano=task_decano, apellido=task_apellido, titulo=task_titulo,
                    descripcion=task_descripcion, direccion=task_direccion)
        task.save()
        return redirect('/Univer/')
    except ValueError as err:
        print(err)
        return redirect('/Univer/')


def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect("/Univer/")

def update(request):
    task_id = request.POST["id"]
    task_decano = request.POST['decano']
    task_apellido = request.POST['apellido']
    task_titulo = request.POST['titulo']
    task_descripcion = request.POST['descripcion']
    task_direccion = request.POST['direccion']  
    task = Task.objects.get(pk=task_id)
    task.decano = task_decano
    task.apellido = task_apellido
    task.titulo = task_titulo
    task.apellido = task_apellido
    task.descripcion = task_descripcion
    task.direccion = task_direccion
    task.save()
    return redirect('/Univer/')


def update_from(request, task_id):
    task = Task.objects.all()
    task_only = Task.objects.get(pk=task_id)
    print(task_only)
    context = {
        "task": task[::-1],
        "update": task_only
    }
    return render(request, 'list_Uni.html', context)