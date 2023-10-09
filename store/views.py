from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product
from django.contrib.auth.forms import UserCreationForm


def categories(request):
    return {
        'categories': Category.objects.all()
    }


def all_categories(request):
    search_term = request.GET.get('search')
    if search_term:
        categories = Category.objects.filter(name__icontains=search_term)
    else:
        categories = Category.objects.all()

    return render(request, 'home.html', {'categories': categories})

def category_products(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'category_products.html', {'category': category, 'products': products})


def product_detail(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    return render(request, 'product_detail.html', {'product': product})






