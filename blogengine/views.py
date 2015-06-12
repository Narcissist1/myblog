from django.shortcuts import render_to_response,render,redirect
from models import Post,Category
from django.core.paginator import Paginator,EmptyPage
from django.template import RequestContext
from django.contrib.syndication.views import Feed
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.db.models import Q

from weibo import APIClient
# Create your views here.


def Signin_weibo(self):
	URL = 'http://codetheme.sinaapp.com'
	APP_KEY = '3328471193'
	APP_SECRET = '08c64d5a6a0e1caee7c2a0a8ef94eeb3'
	CALLBACK_URL = 'http://127.0.0.1:8000/myself/'
	# CALLBACK_URL = URL+'/myself/'
	# CALLBACK_URL='http://open.weibo.com/apps/[id]/info/advanced'

	client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
	url = client.get_authorize_url()
	return HttpResponseRedirect(url)

def getPosts(self,selected_page=1):
	post =Post.objects.all().order_by('-pub_date')

	pages=Paginator(post,5)
	try:
		return_page=pages.page(selected_page)
	except:
		return_page=pages.page(pages.num_pages)
	#display all posts
	return render_to_response('posts.html',{'posts':return_page.object_list,'page':return_page})

def getPost(request,postSlug):
	post=Post.objects.filter(slug=postSlug)
	#display specified post
	return render_to_response('single.html',{'posts':post},context_instance=RequestContext(request))

def infor_self(self):
	return render_to_response('myself.html')

@csrf_exempt
def search_post(request):
	if request.method == "GET":
		value=request.GET.get('value')
		# post=Post.objects.filter(slug=value)
		results = Post.objects.filter(Q(title__icontains=value) | Q(text__icontains=value)).order_by('pub_date')
		return render(request,'single.html',{'posts':results})

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

class PostsFeed(Feed):
    title = "My Django Blog posts"
    link = "feeds/posts/"
    description = "Posts from My Django Blog"

    def items(self):
        return Post.objects.order_by('-pub_date')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text
