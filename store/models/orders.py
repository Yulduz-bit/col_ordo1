from django.db import models
from .product import Product
from .customer import Customer
import datetime
from utils.telegram import send_telegram_message

class Order(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')


    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super().save(*args, **kwargs)

        if is_new:
            message = f"""
    🛍 <b>Новый заказ!</b>
    👤 Клиент: {self.customer.name}
    📱 Телефон: {self.phone}
    📦 Товар: {self.product.name}
    🔢 Количество: {self.quantity}
    💰 Сумма: {self.price} сом
    📍 Адрес: {self.address}
    📅 Дата: {self.date.strftime('%d.%m.%Y')}
    """
            send_telegram_message(message)

