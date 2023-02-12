from django.urls import path
from .views import Signup

urlpatterns = [

    path("register/", Signup, name="signup"),
    
]