import django.contrib.admin
import django.urls
import django.conf


urlpatterns = [
    django.urls.path('', django.urls.include('main.urls')),
    django.urls.path('catalog/', django.urls.include('catalog.urls')),
    django.urls.path('admin/', django.contrib.admin.site.urls),
    django.urls.path('__debug__/', django.urls.include('debug_toolbar.urls')),
]

if django.conf.settings.DEBUG:
    import django.conf.urls.static
    import django.contrib.staticfiles.urls
    
    if django.conf.settings.MEDIA_ROOT:
        urlpatterns += django.conf.urls.static.static(
            prefix=django.conf.settings.MEDIA_URL,
            document_root=django.conf.settings.MEDIA_ROOT,
        )
    urlpatterns += django.contrib.staticfiles.urls.staticfiles_urlpatterns()
