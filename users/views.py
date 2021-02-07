from django.shortcuts import render

# Create your views here.
def login(request):
	page_title = "Knowledge | Connexion"

	if request.method == "POST":
		pass
		"""email = request.POST["email"]
								new_signup = Signup()
								new_signup.email = email
								new_signup.save()"""
	
	context = {
		'page_title': page_title,
	}
	return render(request, "login/login.html", context)

def register(request):
	page_title = "Knowledge | Inscription"

	if request.method == "POST":
		pass
		"""email = request.POST["email"]
								new_signup = Signup()
								new_signup.email = email
								new_signup.save()"""
	
	context = {
		'page_title': page_title,
	}
	return render(request, "login/register.html", context)

def profile(request):
	pass

def settings():
	pass
