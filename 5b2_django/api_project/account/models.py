from doctest import FAIL_FAST
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    gender_choices = (("male", "Male"), ("female", "Female"))
    
 
    gender = models.CharField(max_length=50, null=True, choices=gender_choices)
