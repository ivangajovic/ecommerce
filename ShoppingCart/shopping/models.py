from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User)
    create_date = models.DateTimeField(verbose_name='create date', auto_now=True)
    checked_out = models.BooleanField(default=False, verbose_name='checked out')

    def __str__(self):
        return self.create_date

class Product(models.Model):
        title = models.CharField(max_length = 100, null=True, blank=True)
        description = models.CharField(max_length = 100, null=True, blank=True)
        unit_price = models.DecimalField(max_digits=18, decimal_places=2, verbose_name='unit price')
        total_items = models.IntegerField

        def __str__(self):
            return '%s - %s' % (self.title, self.unit_price)


class Item(models.Model):
    cart = models.ForeignKey(Cart, verbose_name='cart', related_name='cart')
    quantity = models.PositiveIntegerField(verbose_name='quantity')
    product = models.ForeignKey(Product, verbose_name='product', related_name='product')

    def __str__(self):
        return '%d units' % (self.quantity)



