from django.urls import path
from . import views

urlpatterns = [
    path("test/",views.test_view),
    path("about_us/", views.about_us, name="about"),
    path("home/", views.html_home_page, name="home"),
    path("mean/", views.find_mean, name="mean"),
    path("median/", views.median_value, name="median"),
    path("std_dev/", views.standard_deviation, name="std_dev"),
    path("skewness/", views.skewness, name="skewness"),
    
]

