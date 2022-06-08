from django.urls import path, include
from . import views

urlpatterns = [ 
    path("auth/",include('djoser.urls')),
    path("login/", views.LoginView.as_view()),
]