from django.contrib import admin
from core.models import Contact, Newsletter

class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('name', 'email', 'created_date')
    list_filter = ('email',)
    search_fields = ['name', 'message']

class NewsletterAdmin(admin.ModelAdmin):
    list_filter = ('email',)

admin.site.register(Contact, ContactAdmin)
admin.site.register(Newsletter, NewsletterAdmin)

