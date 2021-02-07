from django.db.models import Count, Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentForm, PostModelForm
from .models import Post, Comment, Category, Author
from newsletter.models import Signup


def get_category_count():
	queryset = Post \
		.objects \
		.values('categories__title') \
		.annotate(Count('categories__title')) \
		.order_by('-categories__title__count')

	categories = Category.objects.all()
	for i in range(len(queryset)):
		for cat in categories:
			if cat.title == queryset[i]['categories__title']:
				queryset[i]['url'] = cat.get_absolute_url

	return queryset


def search(request):
	page_title = "Search Results"

	category_count = get_category_count()
	latest = Post.objects.order_by('-timestamp')[0:3]

	queryset = Post.objects.all()
	query = request.GET.get("q")

	if query:
		queryset = queryset.filter(
			Q(title__icontains=query) |
			Q(overview__icontains=query)
		).distinct()
	context = {
		'page_title': page_title,
		'queryset': queryset,
		'query': query,
		'latest' : latest,
		'category_count': category_count,
	}
	return render(request, "blog/search_results.html", context)


def blog(request):
	page_title = "Knowledge | Blog"

	category_count = get_category_count()
	latest = Post.objects.order_by('-timestamp')[0:3]

	post_list = Post.objects.all()
	paginator = Paginator(post_list, 6)
	page_request_var = 'page'
	page = request.GET.get(page_request_var)

	try:
		paginated_queryset = paginator.page(page)
	except PageNotAnInteger:
		paginated_queryset = paginator.page(1)
	except EmptyPage:
		paginated_queryset = paginator.page(paginator.num_pages)

	context = {
		'page_title': page_title,
		'queryset': paginated_queryset,
		'page_request_var': page_request_var,
		'latest' : latest,
		'category_count': category_count,
	}
	return render(request, "blog/blog.html", context)


def post(request, id):
	post = get_object_or_404(Post, id=id)
	comments = Comment.objects.filter(post=id).order_by('timestamp')
	post.comment_count = len(comments)
	page_title = post.title#"Knowledge|{}".format()
	category_count = get_category_count()
	latest = Post.objects.order_by('-timestamp')[0:3]

	"""form = CommentForm(request.POST or None)
				if request.method == "POST":
					if form.is_valid():
						form.instance.user = request.user
						form.instance.post = post
						form.save()"""

	if request.method == "POST":
		comment_post = True
		user = request.user
		content = request.POST["usercomment"]

		comment = Comment()
		comment.user = user
		comment.content = content
		comment.post = post

		comment.save()

		post.comment_count += 1
		
		return redirect('/blog/article/{}/'.format(id)) 

	if request.method == "POST" and not comment_post:
		email = request.POST["email"]
		new_signup = Signup()
		new_signup.email = email
		new_signup.save()

		return redirect('/blog/article/{}/'.format(id))

	context = {
		#'form': form,
		'page_title': page_title,
		'post': post,
		'comment': comments,
		'latest' : latest,
		'category_count': category_count,
	}
	return render(request, "blog/post.html", context)

def create_post(request):
	page_title = "Création d'article"
	author = get_object_or_404(Author , user=request.user)
	categories = Category.objects.all().order_by('title')
	posts = Post.objects.all().filter(author=request.user.author)
	
	"""
	if not author:
		author = Author.objects.create(
		user=request.user,
		first_name=request.user.first_name,
		last_name=request.user.last_name,
		number=request.user.number,
		profile_picture=request.user.profile_picture)
	
	form = PostModelForm(request.POST or None, request.FILES or None)
				if request.method == "POST":
					if form.is_valid:
						form.instance.author = author
						print(form)
						form.save()
						#redirect('blog')"""

	if request.method == "POST":
		"""
		author = request.user.author
		title = request.POST["title"]
		overview = request.POST["overview"]
		categories = request.POST["category"]
		thumbnail = request.POST["thumbnail"]
		previous_post = request.POST["previous"]
		next_post = request.POST["next"]
		"""
		category = request.POST["category"]

		categories = categories.filter(title=category)
		
		post = Post()
		post.title = request.POST["title"]
		post.overview = request.POST["overview"]
		post.categories = categories
		post.thumbnail = request.POST["thumbnail"]
		post.author = request.user.author
		post.previous_post = request.POST["previous"]
		post.next_post = request.POST["next"]

		post.save()
		
		return redirect('/')

		"""
		title
		overview
		thumbnail
		categories
		featured"""

	context = {
		#'form': form,
		'page_title': page_title,
		'categories': categories,
		'posts': posts,
	}
	return render(request, 'blog/create.html', context)



def category(request, id):
	category_count = get_category_count()
	latest = Post.objects.order_by('-timestamp')[0:3]
	
	category = get_object_or_404(Category, id=id)
	page_title = category.title
	post = Post.objects.all()

	queryset = [p for p in post if category in p.categories.all()]

	"""for p in post:
					if p not in queryset:
						del p
				
				paginator = Paginator(queryset, 1)
				page_request_var = 'page'
				page = request.GET.get(page_request_var)
			
				try:
					paginated_queryset = paginator.page(page)
				except PageNotAnInteger:
					paginated_queryset = paginator.page(1)
				except EmptyPage:
					paginated_queryset = paginator.page(paginator.num_pages)"""
	
	context = {
		'page_title': page_title,
		'category': category,
		'queryset': queryset,
		'latest' : latest,
		'category_count': category_count,
	}
	return render(request, "blog/category.html", context) 

def profile(request, id):
	author = get_object_or_404(Author , id=id)
	page_title = author.user.username

	category_count = get_category_count()
	latest = Post.objects.order_by('-timestamp')[0:3]
	
	context = {
		'page_title': page_title,
		#'post': post,
		'author': author,
		'latest' : latest,
		'category_count': category_count,
	}
	return render(request, "blog/profile.html", context)

