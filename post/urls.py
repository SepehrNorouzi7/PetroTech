from django.contrib import admin
from django.urls import path, include
from post.views import *

app_name = 'post'

urlpatterns = [
    path('', post_view, name='index'),
    path('category/<str:cat_name>', post_view, name='category'),
    path('author/<str:author_username>', post_view, name='author'),
    path('<int:pid>', post_single, name='single'),
    path('search/', post_search, name='search'),

]