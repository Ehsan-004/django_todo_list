from django.urls import path
from .views import IndexView, TodoListView, TodoDetailView, NewTodoView, DoTheTask

app_name = 'todos'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('todos/', TodoListView.as_view(), name='todos'),
    path('todos/<str:todo_id>/', TodoDetailView.as_view(), name='todo_detail'),
    path('add_todo/', NewTodoView.as_view(), name='add_todo'),
    path('did_it/', DoTheTask.as_view(), name='did_it'),
]
