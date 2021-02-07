from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()
# Create your models here.

class Author(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=20, default="xxx")
	last_name = models.CharField(max_length=15, default="xxx")
	number = models.CharField(max_length=25, default="XX-XX-XX-XX")
	profile_picture = models.ImageField()

	def full_name(self):
		return self.first_name + " " + self.last_name
	def __str__(self):
		return self.user.username

class Category(models.Model):
	title = models.CharField(max_length=30)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('category-post', kwargs={
			'id': self.id,
			}
		)

class Post(models.Model):
	title = models.CharField(max_length=100)
	overview = models.TextField()
	#content = HTMLField()
	timestamp = models.DateTimeField(auto_now_add=True)
	comment_count = models.IntegerField(default=0)
	view_count = models.IntegerField(default=0)
	author = models.ForeignKey('Author', on_delete=models.CASCADE)
	thumbnail = models.ImageField()
	categories = models.ManyToManyField('Category')
	featured = models.BooleanField(default=False)
	previous_post = models.ForeignKey('self', related_name='previous', on_delete=models.SET_NULL, blank=True, null=True)
	next_post = models.ForeignKey('self', related_name='next', on_delete=models.SET_NULL, blank=True, null=True)
	
	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={
			'id': self.id,
			}
		)

	@property
	def get_comments(self):
		return self.comments.all()
	


class Comment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	
	timestamp = models.DateTimeField(auto_now_add=True)
	content = models.TextField()
	post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)

	def __str__(self):
		return self.user.username