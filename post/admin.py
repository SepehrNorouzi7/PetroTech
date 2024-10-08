from django.contrib import admin
from post.models import Post, Category
from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title', 'counted_views', 'status', 'published_date')
    list_filter = ('status',)
    search_fields = ['title', 'content']
    summernote_fields = ('content',)

admin.site.register(Category)
admin.site.register(Post, PostAdmin)