from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Receipe(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True, blank=True)
    rec_name=models.CharField(max_length=100)
    rec_desc=models.TextField()
    rec_image=models.ImageField(upload_to="receipe")
