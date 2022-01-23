from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
     path('', views.show, name='show'),
    path('insert', views.insert, name='insert'),
    path('delete<int:id>', views.delete, name='delete'),
    path('update<int:id>', views.update, name='update'),
    path('index',views.index, name='index'),
    path('login',views.loginuser, name='loginuser'),
    path('logout',views.logoutuser, name='logout')
   
]