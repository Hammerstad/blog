from django.shortcuts import render

from app.blog.forms import PostForm

def home(request):
	return render(request, 'home.html')
	
def new(request):
	if request.POST:
		post_form = PostForm(request)
	else:
		post_form = PostForm()
	
	return render(request, 'post/new.html', locals())