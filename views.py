from todo.models import Todo
from django.shortcuts import render
from .forms import TodoForm
# Create your views here.
def index(request):
    obj = Todo.objects.all()
    params = {
      'title': 'Todo',
      'todo' : obj,
    }
    return render(request, 'todo/index.html',params)
def create(request):
  if(request.method == 'POST'):
    obj = Todo()
    todo = TodoForm(request.POST, instance=obj)
    todo.save()
    # return redirect(to='/todo')
  params = {
    'title': 'Todo',
    'form':TodoForm(),
  }
  return render(request,'todo/create.html',params)

def edit(request,num):
  obj = Todo.objects.get(id=num)
  if(request.method == 'POST'):
    todo = TodoForm(request.POST, instance=obj)
    todo.save()
    # return redirect(to='/todo')
  params = {'title': 'Todo', 
            'id':num, 
            'form':TodoForm(instance=obj),
  }
  return render(request,'todo/edit.html',params)

def delete(request,num):
   todo = Todo.objects.get(id=num)
   if (request.method == 'POST'):
     todo.delete()
    #  return redirect(to='/todo')
   params = {'title': 'Todo',
              'id':num,
              'obj':todo,
            }
   return render(request,'todo/delete.html',params)

