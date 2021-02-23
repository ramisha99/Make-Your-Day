from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from .models import*
from .form import*


def index(request):
    todolist= Todolist.objects.all()

    form=TodolistForm()

    if request.method == 'POST':#user wants to post something
        form=TodolistForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect ('/') # after posting it goes back to the same template

    context = {'todolist': todolist, 'form': form}
    return render(request, 'todolist/list.html', context)


def updateTask(request,pk):#pk is the primary key
    todolist=Todolist.objects.get(id=pk)

    form = TodolistForm(instance=todolist)
    if request.method == 'POST':
        form = TodolistForm(request.POST, instance=todolist)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}

    return render(request, 'todolist/update_task.html', context)

def deleteTask(request, pk):
	item = Todolist.objects.get(id=pk)

	if request.method == 'POST':
		item.delete()
		return redirect('/')

	context = {'item':item}
	return render(request, 'todolist/delete.html', context)

