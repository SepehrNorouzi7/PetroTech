from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from core.sitemaps import StaticViewSitemap
from post.sitemaps import BlogSitemap
from debug_toolbar.toolbar import debug_toolbar_urls

sitemaps = {
    "static": StaticViewSitemap,
    "post": BlogSitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('account/', include('account.urls')),
    path('post/', include('post.urls')),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="django.contrib.sitemaps.views.sitemap",
    ),
    path('robots.txt', include('robots.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('captcha/', include('captcha.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += debug_toolbar_urls()
