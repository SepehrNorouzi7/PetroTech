from django.contrib import admin
from django.urls import path, include
from core.views import *

app_name = 'core'

urlpatterns = [
    path('', index_view, name='index'),
    path('about', about_view, name='about'),
    path('contact', contact_view, name='contact'),
]