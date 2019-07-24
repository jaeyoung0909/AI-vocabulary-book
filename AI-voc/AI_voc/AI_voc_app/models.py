from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Vocabulary (models.Model):
    word = models.CharField(max_length=30)

class Ability (models.Model):
    word = models.ForeignKey(Vocabulary, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ability = models.IntegerField(default= 0)

class Dictionary (models.Model):
    word = models.CharField(max_length=30, default='')
    meaning = models.CharField(max_length=30, default='')
