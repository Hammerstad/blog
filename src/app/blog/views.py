from django.shortcuts import render, redirect, get_object_or_404

from app.blog.forms import PostForm
from app.blog.models import Post

def home(request):
	return render(request, 'home.html')
	
def new_post(request):
	if request.method == 'POST':
		post_form = PostForm(request.POST)
		if post_form.is_valid():
			post = post_form.save(commit = False)
			post.creator = request.user
			post.save()
	else:
		post_form = PostForm()
	
	return render(request, 'post/new.html', locals())
	
def view_post(request, id):
	post = get_object_or_404(Post, id=id)
	return render(request, 'post/view.html', locals())