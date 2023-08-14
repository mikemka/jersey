from django.contrib.admin import ModelAdmin, register
from catalog import models


@register(models.Category)
class CategoryAdmin(ModelAdmin):
    list_display = ('title', 'admin_thumbnail')
    list_display_links = ('title', 'admin_thumbnail')


@register(models.Product)
class ProductAdmin(ModelAdmin):
    list_display = ('title', 'category', 'admin_thumbnail', 'price')
    list_display_links = ('title', 'category', 'admin_thumbnail', 'price')


@register(models.Image)
class ImageAdmin(ModelAdmin):
    list_display = ('product', 'admin_thumbnail')
    list_display_links = ('product', 'admin_thumbnail')

@register(models.Size)
class SizeAdmin(ModelAdmin):
    list_display = ('size', 'size_category',)
    list_display_links = ('size', 'size_category',)


@register(models.SizeCategory)
class SizeCategoryAdmin(ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)
