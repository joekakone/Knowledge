from django.shortcuts import render

# Create your views here.

def news(request):
	page_title = 'Actualités'
	context = {
		'page_title': page_title,
	}
	return render(request, 'news/news.html', context)