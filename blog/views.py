from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from blog.models import Post, Comment, Category
from blog.forms import CommentForm

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
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)
    
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": CommentForm(),
    }
    return render(request, "blog/detail.html", context)