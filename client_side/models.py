from django.db import models

from driver_side.models import Car
from driver_side.models import Driver
from driver_side.models import Street

# Create your models here.

GENDER_CLIENT_CHOICES = [
    ('Ж', 'женский'),
    ('М', 'мужской')
]

STATUS_ORDER_CHOICES = [
    ('ожидается', 'ожидается'),
    ('отменён', 'отменён'),
    ('в процессе', 'в процессе'),
    ('завершён', 'завершён')
]

CAR_CLASS_ORDER_CHOICES = [
    ('эконом', 'эконом'),
    ('комфорт', 'комфорт'),
    ('премиум', 'премиум')
]

class Client(models.Model):
    full_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=15, choices=GENDER_CLIENT_CHOICES)
    login = models.CharField(max_length=15)
    password = models.CharField(max_length=10)
    def __str__(self):
        return self.full_name

class Operator(models.Model):
    full_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=15, choices=GENDER_CLIENT_CHOICES)
    def __str__(self):
        return self.full_name

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    operator = models.ForeignKey(Operator, on_delete=models.CASCADE)
    order_time = models.DateTimeField()
    status = models.CharField(max_length=15, choices=STATUS_ORDER_CHOICES)
    from_place = models.ForeignKey(Street, on_delete=models.PROTECT, related_name='from_place')
    to_place = models.ForeignKey(Street, on_delete=models.PROTECT, related_name='to_place')
    car_class = models.CharField(max_length=15, choices=CAR_CLASS_ORDER_CHOICES)
    driver_gender = models.CharField(max_length=15, choices=GENDER_CLIENT_CHOICES)
    def __str__(self):
        return str(self.id)

class Ride(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    duration = models.PositiveIntegerField()
    mileage = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)

class DiscountCard(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    points = models.PositiveIntegerField()
    def __str__(self):
        return str(self.id)