from django.urls import path
from . import views

urlpatterns = [
    path("test/",views.test_view),
    path("about_us/", views.about_us, name="about"),
    path("home/", views.html_home_page, name="home"),
    path("contact/", views.contact_us, name="contact")
]

