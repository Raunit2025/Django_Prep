from django.urls import path
from . import views

urlpatterns = [
    path("id/<int:id>/<str:name>/", views.index, name="index"),
    path("user/<str:username>/",views.user, name="user" ),
    path("user_details/<str:name>/<int:age>/<str:color>/",views.user_details, name="user_details"),
    path("products/",views.products,name="products")
]