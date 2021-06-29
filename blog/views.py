from django.shortcuts import render , get_object_or_404

from .models import Blog

def allblogs(request):

	blogs = Blog.objects
	return render(request, 'blog/allblogs.html' , {'blogs':blogs})

def detail(request, blogid):
	detailblog = get_object_or_404(Blog, pk = blogid)    #pk = primary key
	return render(request, 'blog/detail.html', {'blog':detailblog})