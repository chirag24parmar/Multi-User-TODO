from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from app.views import home ,login ,signup, add_todo, signout, delete_todo, change_todo

urlpatterns = [
    path('', home , name='home'),
    path('login',login, name='login'),
    path('signup',signup, name='signup'),
    path('add_todo',add_todo),
    path('delete_todo/<int:id>',delete_todo),
    path('change_todo/<int:id>/<str:status>',change_todo),
    path('logout',signout),
]
