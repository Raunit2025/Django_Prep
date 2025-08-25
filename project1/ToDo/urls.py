from django.urls import path
from . import views

urlpattern = [
    path('',views.index,name='index'),
    path('add/',views.add_todo, name='add_todo'),
    path('complete/<int:id>/', views.complete_todo, name='complete_todo'),
    path('delete/<int:id>/', views.delete_todo, name='delete_todo')
]