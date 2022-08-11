from cart.forms import CartAddProductForm
from django.shortcuts import get_object_or_404, render

from .models import Product, ProductImage

def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    photos = ProductImage.objects.filter(product=product)
                                
    cart_product_form = CartAddProductForm()
    return render(request, 'product.html', {
        'product': product,
        'cart_product_form': cart_product_form,
        'photos': photos,
        })
