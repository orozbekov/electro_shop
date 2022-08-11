from tabnanny import verbose
from turtle import up, update
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.db import models

class Category(models.Model):
    """Категория"""
    title = models.CharField("Категория", max_length=150, blank=False)
    description = models.TextField("Описание", blank=True)
    slug = models.SlugField("URL", max_length=100, unique=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_list_by_category',
                        args=[self.slug])


class Product(models.Model):
    """Товар"""
    category = models.ForeignKey(to=Category, verbose_name="Категория", related_name="products", on_delete=models.CASCADE)
    name = models.CharField("Название товара", max_length=250)
    slug = models.SlugField("URL", max_length=150, unique=True) 
    image = models.ImageField("Изображение", blank=True)
    description = models.TextField("Описание", blank=True)
    body = RichTextField("Характеристики", blank=True)
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField("Количество товара")
    sale = models.IntegerField("Скидка в процентах", blank=True, default=0)
    available = models.BooleanField("Активный", default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail',
                        args=[self.id, self.slug])

    def get_sale(self):
        """
        Расчитать стоимость со скидкой
        """
        price = int(self.price * (100 - self.sale) / 100)
        return price

class ProductImage(models.Model):
    """Изображение"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField("Изображение", upload_to='products/', blank=True)

    class Meta:
        verbose_name = "Изображение продукта"
        verbose_name_plural = "Изображение продукта"

    def __str__(self):
        return self.product.name


    