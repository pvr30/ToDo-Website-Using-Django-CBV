from django.shortcuts import render
from django.views.generic import (TemplateView,ListView,
                                 CreateView,UpdateView,
                                 DeleteView,)
from todo import models
from todo.models import Task
from django.urls import reverse_lazy
from todo import forms
# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'

class TaskList(ListView):
    context_object_name = 'task_list'
    model = models.Task
    template_name = 'task_list.html'

class AddTask(CreateView):
    fields = ('title','description')
    model = models.Task
    template_name = 'add_task.html'

class UpdateTask(UpdateView):
    fields = ('title','description')
    model = models.Task
    template_name = 'add_task.html'

class DeleteTask(DeleteView):
    context_object_name = 'task'
    model = models.Task
    success_url = reverse_lazy('task_list')
    template_name = 'task_confirm_delete.html'

class Login(TemplateView):
    template_name = 'login.html'

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = 'sign_up.html'