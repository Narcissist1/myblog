from django.shortcuts import render_to_response
from models import Post
from django.core.paginator import Paginator
# Create your views here.

def getRecentPosts(self):
	posts=Post.objects.all()

	sorted_post=posts.order_by('-pub_date')

	return render_to_response('posts.html',{'posts':sorted_post})

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
