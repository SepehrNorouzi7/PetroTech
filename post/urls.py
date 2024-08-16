from django.contrib import admin
from django.urls import path, include
from post.views import *

app_name = 'post'

urlpatterns = [
    path('', post_view, name='index'),
    path('single', post_single, name='single'),

]