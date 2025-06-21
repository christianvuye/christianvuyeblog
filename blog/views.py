from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category

def blog_index(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {
        "posts": posts,
    }
    return render(request, "blog/index.html", context)

def blog_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.all().order_by("-created_on") # type: ignore
    context = {
        "category": category,
        "posts": posts,
    }
    return render(request, "blog/category.html", context) 

def blog_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {
        "post": post,
    }
    return render(request, "blog/detail.html", context)

def about(request):
    return render(request, "blog/about.html")