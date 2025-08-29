from django.urls import path
from . import views

urlpatterns = [
    path("id/<int:id>/<str:name>/", views.index, name="index"),
    path("user/<str:username>/",views.user, name="user" )
]