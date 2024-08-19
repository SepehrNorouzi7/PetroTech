from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from post.models import Post

def post_view(request):
    posts = Post.objects.filter(status=1)
    context = {'posts': posts}
    return render(request, 'post/blog-home.html', context)

def post_single(request, pid):
    posts = Post.objects.filter(status=1)
    post = get_object_or_404(posts, pk=pid)
    context = {'post': post}
    return render(request, 'post/blog-single.html', context)