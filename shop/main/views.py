from django.shortcuts import render
from catalog.models import Category


def homepage(request):
    template_name = 'main/homepage.html'
    extra = {
        'categories': Category.objects.all()[:6]
    }

    return render(
        request=request,
        template_name=template_name,
        context=extra,
    )
