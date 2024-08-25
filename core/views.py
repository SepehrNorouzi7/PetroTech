from django.shortcuts import render
from django.http import HttpResponseRedirect
from core.forms import ContactForm, NewsletterForm
from django.contrib import messages
from post.models import Post

def index_view(request, **kwargs):
    posts = Post.objects.filter(status=1)
    if kwargs.get('cat_name') is not None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('tag_name') is not None:
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])
    if kwargs.get('author_username') is not None:
        posts = posts.filter(author__username=kwargs['author_username'])
    context = {'posts': posts}
    return render(request, 'index.html', context)

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your ticket submited successfully')
        else:
            messages.add_message(request, messages.ERROR, 'Your ticket did not submited successfully')
    form = ContactForm()
    return render(request, 'contact.html')

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')