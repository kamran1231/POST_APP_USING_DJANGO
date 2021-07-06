from django.db import models
from django.contrib.auth.models import User
from .forms import SignupForm
# Create your models here.




class User_Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.user)