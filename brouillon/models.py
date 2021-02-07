from django.db import models

# Create your models here.
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Auteur(models.Model):
	utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
	email = models.EmailField()

	def __str__(self):
		return self.utilisateur.username


class Categorie(models.Model):
	nom = models.CharField(max_length=50, unique=True)

	def __str__(self):
		return self.nom.upper()


class Article(models.Model):
	titre = models.CharField(max_length=120)
	contenu = models.TextField()
	auteur = models.ForeignKey(Auteur, on_delete=models.CASCADE)
	image = models.ImageField()
	slug = models.SlugField()
	date = models.DateField()

	def __str__(self):
		return self.titre


class Commentaire(models.Model):
	article = models.ForeignKey(Article, on_delete=models.CASCADE)
	auteur = models.ForeignKey(User, on_delete=models.CASCADE)
	contenu = models.TextField()
	date = models.DateField()

	def __str__(self):
		th = " ".join(self.contenu.split()[:5]) + " ..."
		return th
