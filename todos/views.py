from django.shortcuts import render, redirect
from django.views import View
from .models import Task
from django.utils.timezone import now


class IndexView(View):
    http_method_names = ['get', 'post']
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)


class TodoListView(View):
    http_method_names = ['get', 'post']
    template_name = 'todos_list.html'

    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('todo_user:login')
        todos_list = []
        user = request.user
        todos = Task.objects.filter(user=user).order_by('-start_date')
        for todo in todos:
            todos_list.append({
                'id': todo.id,
                'title': todo.title,
                'description': todo.description,
                'done': todo.done,
                'start_date': todo.start_date,
                'end_date': todo.end_date,
            })
        return render(request, self.template_name, {'todo_list': todos_list})


class TodoDetailView(View):
    http_method_names = ['get', 'post']
    template_name = 'single_todo.html'

    def get(self, request, todo_id):
        if not request.user.is_authenticated:
            return redirect('todo_user:login')
        todo_id = int(self.kwargs.get('todo_id', False))
        if not todo_id:
            return redirect('todo_user:index')
        todo = Task.objects.get(id=todo_id)
        return render(request, self.template_name, {'todo': todo})


class NewTodoView(View):
    http_method_names = ['get', 'post']
    template_name = 'add_task.html'

    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('todo_user:login')
        return render(request, self.template_name)

    def post(self, request):
        if not request.user.is_authenticated:
            return redirect('todo_user:login')
        title = request.POST.get('title', False)
        description = request.POST.get('description', False)
        start_date = request.POST.get('start_date', False)

        if not start_date:
            start_date = now()

        if False in [title, description, start_date]:
            return render(request, self.template_name, {'error': 'Please enter all fields'})
        todo = Task.objects.create(title=title, description=description, start_date=start_date, user=request.user)
        return redirect('todos:todos')


class DoTheTask(View):
    http_method_names = ['post',]

    def post(self, request):
        if not request.user.is_authenticated:
            return redirect('todo_user:login')
        todo_id = request.POST.get('task_id', False)
        user = request.user
        if not todo_id:
            return redirect('todos:todos')
        task = Task.objects.get(id=todo_id)
        task.done = 1
        task.save()
        return redirect('todos:todos')
