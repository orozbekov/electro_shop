from django.db import models

from apps.shop.models import Product

class Order(models.Model):
    """Модель для заказа товаров"""
    first_name = models.CharField("Имя", max_length=50)
    last_name = models.CharField("Фамилия", max_length=50)
    email = models.EmailField("Электронный адрес", blank=True)
    address = models.CharField("Адрес", max_length=250)
    postal_code = models.CharField("Почтовый индекс", max_length=20)
    city = models.CharField("Город", max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)   

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f"Заказ {self.id}"

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, null=True, related_name='items', on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, related_name='order_items', on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.id}"

    def get_cost(self):
        return self.price * self.quantity