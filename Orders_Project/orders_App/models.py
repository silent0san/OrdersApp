from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
import uuid




class OrderedDish(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField('Dish name', max_length=150, default='')
    price = models.PositiveSmallIntegerField()
    owner = models.CharField(max_length=150, default='', blank=False)
    created_date = models.DateTimeField('Created Date', default=now, editable=False)

    def __str__(self):
        return self.name


class Dish(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField('Dish name', max_length=150, default='')
    price = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateField()
    dishes = models.ManyToManyField(Dish, blank=True)
    sum = models.PositiveSmallIntegerField()


#class DishList(models.Model):
#    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#    date = models.DateField()
#    name = models.CharField('Dish name', max_length=150, default='')

# class Persons_Order(models.Model):
#   id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#    sum = models.PositiveSmallIntegerField()
#    dishes = models.ManyToManyField(Dish, blank=True)
