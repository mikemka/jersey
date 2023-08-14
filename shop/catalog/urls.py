import django.urls
import catalog.views


urlpatterns = [
    django.urls.path('', catalog.views.categories, name='categories'),
    django.urls.path('<int:pk>/', catalog.views.category, name='category'),
    django.urls.path('<int:pk>/<int:product_id>/', catalog.views.product, name='product'),
]
