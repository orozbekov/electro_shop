from django.shortcuts import render

from django.shortcuts import get_object_or_404, redirect, render

from .cart import Cart
from .forms import CartAddProductForm
from apps.shop.models import Product

def cart_add(request, slug):
    cart = Cart(request)
    product = get_object_or_404(Product, slug=slug)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('home')

def item_clear(request, slug):
    cart = Cart(request)
    product = get_object_or_404(Product, slug=slug)
    cart.remove(product=product)
    return redirect('home')

def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect('home')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'blank.html', {'cart': cart})
