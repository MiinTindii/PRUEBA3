from django.urls import path
from django.views.generic.base import View
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleteView, Login, RegisterPage
from .views import index, t1, buscador, contacto, login, mazdarx8, quieness, skyline350gt, t2, t3, terms
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', index, name="index"),
    path('t1/', t1, name="t1"),
    path('buscador/', buscador, name="buscador"),
    path('contacto/', contacto, name="contacto"),
    path('login/', login, name="login"),
    path('mazdarx8/', mazdarx8, name="mazdarx8"),
    path('quieness/', quieness, name="quieness"),
    path('skyline350gt/', skyline350gt, name="skyline350gt"),
    path('t2/', t2, name="t2"),
    path('t3/', t3, name="t3"),
    path('terms/', terms, name="terms"),
    path('task', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', DeleteView.as_view(), name='task-delete'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
]