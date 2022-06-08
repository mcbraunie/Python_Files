from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from myblog.models import Post, Category
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer, PostSerializer, CategorySerializer


def detail_view(request, post_id):
	published = Post.objects.exclude(published_date__exact=None)
	try:
		post = published.get(pk=post_id)
	except Post.DoesNotExist:
		raise Http404
	context = {'post': post}
	return render(request, 'detail.html', context)

def list_view(request):
	published = Post.objects.exclude(published_date__exact=None)
	posts = published.order_by('-published_date')
	context = {'posts': posts}
	return render(request, 'list.html', context)

def stub_view(request, *args, **kwargs):
	body = "Stub View\n\n"
	if args:
		body += "Args:\n"
		body += "\n".join(["\t%s" % a for a in args])
	if kwargs:
		body += "Kwargs:\n"
		body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])
	return HttpResponse(body, content_type="text/plain")


class UserViewSet(viewsets.ModelViewSet):
	"""
	The hub for the User portion of the API, allowing for the
	users in the app to be viewed/edited
	"""
	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
	"""
	The hub for the Groups portion of the API, allowing for the
	groups in the app to be viewed/edited
	"""
	queryset = Group.objects.all()
	serializer_class = GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
	"""
	The hub for the Post portion of the API, allowing for the
	posts in the app to be viewed/edited
	"""
	queryset = Post.objects.all().order_by('created_date')
	serializer_class = PostSerializer


class CategoryViewSet(viewsets.ModelViewSet):
	"""
	The hub for the Category portion of the API, allowing for the
	categories in the app to be viewed/edited
	"""
	queryset = Category.objects.all()
serializer_class = CategorySerializer