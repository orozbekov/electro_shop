from django.shortcuts import render, get_object_or_404

from apps.cart.forms import CartAddProductForm
from .models import Category, Product, ProductImage

# Страница с товарами
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'index.html', {
        'category': category,
        'categories': categories,
        'products': products
    })

# Страница товара
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    photos = ProductImage.objects.all()
    cart_product_form = CartAddProductForm()
    return render(request, 'product.html',
                             {'product': product,
                              'photos': photos, 
                              'cart_product_form': cart_product_form
                              })