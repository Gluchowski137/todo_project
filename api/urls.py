from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('todos', views.TodoCreate.as_view()),
    path('todos/completed', views.TodoCompleted.as_view()),
    path('todos/<int:pk>', views.TodoRetrieveUpdateDestroy.as_view()),
    path('todos/<int:pk>/completed', views.TodoComplete.as_view()),

    path('signup',views.signup),
    path('login', views.login),

]
