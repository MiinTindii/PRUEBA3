from django.forms import fields
from django.forms.models import fields_for_model
from core.models import Task
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView
from django.urls import reverse_lazy
from .models import Task
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


    

def index(request):
    return render(request, 'core/index.html')

def t1(request):
    return render(request, 'core/t1.html')

def buscador(request):
    return render(request, 'core/buscador.html')

def contacto(request):
    return render(request, 'core/contacto.html')

def login(request):
    return render(request, 'core/login.html')

def mazdarx8(request):
    return render(request, 'core/mazdarx8.html')

def quieness(request):
    return render(request, 'core/quieness.html')

def skyline350gt(request):
    return render(request, 'core/skyline350gt.html')

def t2(request):
    return render(request, 'core/t2.html')

def t3(request):
    return render(request, 'core/t3.html')

def terms(request):
    return render(request, 'core/terms.html')
        
class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(
                title__startswith=search_input)

        context['search_input'] = search_input

        return context

class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'core/task.html'

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')

class DeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')

class Login(LoginView):
    template_name = "core/login.html"
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')

class RegisterPage(FormView):
    template_name = 'core/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPage, self).get(*args, **kwargs)