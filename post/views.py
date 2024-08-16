from django.shortcuts import render
from django.http import HttpResponse

def post_view(request):
    return render(request, 'post/blog-home.html')

def post_single(request):
    return render(request, 'post/blog-single.html')