from django.contrib import admin
from django.urls import path , include

from . import views

urlpatterns = [

    path('login' , views.LoginView.as_view() , name="login" ),
    path('signup' , views.SignupView.as_view() , name="signup" ),
    path('logout' , views.logout_view , name="logout" ),

]