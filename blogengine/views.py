from django.shortcuts import render_to_response
from models import Post,Category
from django.core.paginator import Paginator,EmptyPage
# Create your views here.

def getPosts(self,selected_page=1):
	post =Post.objects.all().order_by('-pub_date')

	pages=Paginator(post,5)
	try:
		return_page=pages.page(selected_page)
	except:
		return_page=pages.page(pages.num_pages)
	#display all posts
	return render_to_response('posts.html',{'posts':return_page.object_list,'page':return_page})

def getPost(self,postSlug):
	post=Post.objects.filter(slug=postSlug)
	#display specified post
	return render_to_response('single.html',{'posts':post})

def getCategory(request,categorySlug,selected_page=1):
	posts =Post.objects.all().order_by('-pub_date')

	category_posts = []
	for post in posts:
		if post.categories.filter(slug=categorySlug):
			category_posts.append(post)

	pages = Paginator(category_posts, 5)
	# Get the category
	category = Category.objects.filter(slug=categorySlug)[0]
	# Get the specified page
	try:
		returned_page=pages.page(selected_page)
	except EmptyPage:
		returned_page=pages.page(pages.num_pages)

	# Display all the posts
	return render_to_response('category.html', {'posts': returned_page.object_list, 'page': returned_page, 'category': category})
