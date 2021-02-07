from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model(models.Model)

class Forum:
	user = models.OneToOneField(User, on_delete=models.CASCADE)



class Message(models.Model):
	author