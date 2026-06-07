# orders/models.py

from django.db import models
from django.contrib.auth.models import User


class FoodItem(models.Model):

    name = models.CharField(max_length=200)

    description = models.TextField()

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    image = models.ImageField(
        upload_to='food_images/'
    )

    def __str__(self):
        return self.name


class Cart(models.Model):

    food_item = models.ForeignKey(
        FoodItem,
        on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField(
        default=1
    )

    def __str__(self):
        return f"{self.food_item.name} - {self.quantity}"


class Order(models.Model):

    address = models.JSONField()

    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Order {self.id}"


class OrderItem(models.Model):

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items'
    )

    food_item = models.ForeignKey(
        FoodItem,
        on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.food_item.name} x {self.quantity}"


class UserAddress(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    name = models.CharField(
        max_length=100
    )

    phone = models.CharField(
        max_length=15
    )

    area = models.CharField(
        max_length=255
    )

    city = models.CharField(
        max_length=100
    )

    landmark = models.CharField(
        max_length=255,
        blank=True
    )

    district = models.CharField(
        max_length=100
    )

    zipcode = models.CharField(
        max_length=10
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name