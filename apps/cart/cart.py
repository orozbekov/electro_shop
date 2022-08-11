from decimal import Decimal

from django.conf import settings


class Cart(object):

    def __init__(self, request):
        """
        Инициализируем корзину
        """
        self.request = request
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # сохранение пустую корзину в сеансе
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity, update_quantity=False):
        """
        Добавить продукт в корзину или обновить его количество.
        """
        id = product.id 
        if str(product.id) not in self.cart:

            self.cart[product.id] = {
                'user_id': self.request.user.id,
                'product_id': id,
                'product_slug': product.slug,
                'product_name': product.name,
                'quantity': 0,
                'price': product.price,
                'image': product.image.url
            }

            self.cart[product.id]['quantity'] += quantity

        else:

            for key, value in self.cart.items():
                if key == str(product.id):
                    if update_quantity:
                        value['quantity'] = quantity
                        self.save()
                        break
                    else:
                        value['quantity'] += quantity
                        self.save()
                        break
        self.save()

    def save(self):
        # Обновление сессии cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # Отметить сеанс как "измененный", чтобы убедиться, что он сохранен
        self.session.modified = True

    def remove(self, product):
        """
        Удаление товара из корзины.
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def get_total_price(self):
        """
        Подсчет стоимости товаров в корзине.
        """
        return sum(Decimal(item['price']) * item['quantity'] for item in
                self.cart.values())

    def clear(self):
        # удаление корзины из сессии
        self.session[settings.CART_SESSION_ID] = {}
        self.session.modified = True