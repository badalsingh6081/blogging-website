from django.db import models
from django.contrib.auth.models import User




class blog(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE )
    name=models.CharField( max_length=50)
    date=models.DateField()
    title=models.CharField(max_length=100)
    desc=models.TextField()
