from django.shortcuts import render, redirect
from posts.models import Post
from newsletter.models import Signup


def index(request):
	page_title = "Knowledge | Accueil"
	featured = Post.objects.filter(featured=True).order_by('-comment_count')[0:4]
	latest = Post.objects.order_by('-timestamp')[0:3]

	if request.method == "POST":
		email = request.POST["email"]
		new_signup = Signup()
		new_signup.email = email
		new_signup.save()

		return redirect('/')
	
	context = {
		'page_title': page_title,
		'object_list': featured,
		'latest' : latest,
	}

	return render(request, "index.html", context)
