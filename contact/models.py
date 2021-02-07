from django.db import models

# Create your models here.

class Message(models.Model):
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=15)
	email = models.EmailField()
	number = models.CharField(max_length=15, default="00228 96273390")
	message = models.TextField()
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.first_name + " " + self.last_name