from django.shortcuts import render, redirect
from contact.models import Message

# Create your views here.
def contact(request):
	page_title = "Knowledge | Contact"

	if request.method == "POST":
		first_name = request.POST["first_name"]
		last_name = request.POST["last_name"]
		email = request.POST["email"]
		message = request.POST["message"]
		number = request.POST["number"]

		new_message = Message()
		new_message.first_name = first_name
		new_message.last_name = last_name
		new_message.email = email
		new_message.message = message
		new_message.number = number
		new_message.save()

		return redirect('/')
	
	context = {
		'page_title': page_title,
	}
	return render(request, "contact.html", context)

def contact_message(request):
	page_title = "Message envoyé avec succès"

	context = {
		'page_title': page_title,
	}

	return render(request, "messages/contact_message.html", context)