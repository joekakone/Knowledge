from django.shortcuts import render

# Create your views here.
def newsletter(request):
	page_title = "Abonnement réussi"

	context = {
		'page_title': page_title,
	}

	return render(request, "messages/newsletter.html", context)