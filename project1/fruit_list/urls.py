from django.urls import path
from . import views

urlpatterns = [
    path('fruits/' ,views.fruit_list, name='fruit_list'),
    path('home/', views.home, name='home'),
    path('monday/', views.monday_special, name='monday_special'),
    path('tuesday/', views.tuesday_special, name='tuesday_specail')
]