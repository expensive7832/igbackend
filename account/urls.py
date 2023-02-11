from django.urls import path
from .views import Signup, Login, Update, getAllUser, getUser, Delete

urlpatterns = [

    path("register/", Signup, name="signup"),
    path("login/", Login, name="login"),
    path("update/", Update, name="update"),
    path("delete/", Delete, name="delete"),
    
]