from django.contrib import admin

from .models import Category, Product, ProductImage

class ProductImageAdmin(admin.StackedInline):
    model = ProductImage

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]
    list_display = ('name', 'category')
    prepopulated_fields = {'slug': ('name',)}
    
    class Meta:
        model = Product
