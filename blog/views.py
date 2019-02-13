from django.shortcuts import render, redirect
from .models import Blog

# Create your views here.

def blog(request):
    blog = Blog.objects.all()
    return render(request, 'blog/blog.html',{'blogs':blog})

def form(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('form')
    else:
        form = PostForm()
    return render(request,'blog/form_blog.html', {'form': form})