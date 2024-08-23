from django.shortcuts import render
from django.http import HttpResponseRedirect
from core.forms import ContactForm, NewsletterForm
from django.contrib import messages

def index_view(request):
    return render(request, 'index.html')

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'your ticket submited successfully')
        else:
            messages.add_message(request, messages.ERROR, 'your ticket did not submited successfully')
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