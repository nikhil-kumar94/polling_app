from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.question ),
    path('question/<str:pk>',views.question_choices),
    
]