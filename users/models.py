from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):    
    country = models.CharField(max_length=30, null=True, blank=False) 
    state = models.CharField(max_length=30, null=True, blank=False)
    
  
