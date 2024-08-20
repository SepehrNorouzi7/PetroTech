from django import template
from post.models import Post, Category

register = template.Library()

@register.inclusion_tag('post/blog-popular-post.html')
def latestPosts(arg=4):
    posts = Post.objects.filter(status=1).order_by('published_date')[:arg]
    return {'posts': posts}

@register.inclusion_tag('post/blog-category.html')
def postCategories():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name]=posts.filter(category=name).count()
    return {'categories': cat_dict}