from django.shortcuts import render, get_object_or_404
from catalog.models import Category, Product, Image, Size


def categories(request):
    template_name = 'catalog/categories.html'
    extra = {
        'categories': Category.objects.order_by('-id'),
    }

    return render(
        request=request,
        template_name=template_name,
        context=extra,
    )


def category(request, pk: int):
    template_name = 'catalog/category.html'
    category = get_object_or_404(Category, id=pk)
    extra = {
        'category': category,
        'products': Product.objects.filter(category=category),
    }

    return render(
        request=request,
        template_name=template_name,
        context=extra,
    )


def product(request, pk: int, product_id: int):
    template_name = 'catalog/product.html'
    category = get_object_or_404(Category, id=pk)
    product = get_object_or_404(Product, id=product_id, category=category)
    product_sizes = product.sizes.all()
    all_sizes = Size.objects.filter(size_category=product_sizes[0].size_category) if product_sizes else []
    extra = {
        'category': category,
        'product': product,
        'product_sizes': product_sizes,
        'all_sizes': all_sizes,
        'images': Image.objects.filter(product=product),
    }

    return render(
        request=request,
        template_name=template_name,
        context=extra,
    )
