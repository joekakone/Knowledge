from django.db import models
from django.urls import reverse

# Create your models here.
class Role(models.Model):
	title = models.CharField(max_length=20)

	def __str__(self):
		return self.title

class Member(models.Model):
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=15)
	"""facebook = models.UrlField()
				google = models.UrlField()
				twitter = models.UrlField()
				linkedin = models.UrlField()"""
	roles = models.ManyToManyField(Role)
	level = models.IntegerField(default=5)
	email = models.EmailField()
	number = models.CharField(max_length=15, default="00228 96273390")
	description = models.TextField(default="Pellentesque habitant morbi tristique senectus\
		et netus et malesuada fames ac turpis egestas.")
	profile_picture = models.ImageField()

	def __str__(self):
		return self.first_name + " " + self.last_name

	def get_absolute_url(self):
		return reverse('team-member', kwargs={
			'id': self.id,
			}
		)

	def get_fullname(self):
		return self.first_name + " " + self.last_name