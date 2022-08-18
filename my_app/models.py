from django.db import models
import datetime


class User(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email


class Client(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Worker(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    extra_price = models.IntegerField()

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=100)
    start_price = models.IntegerField()
    ingredients = models.ManyToManyField(Ingredient, through='Order')
    clients = models.ManyToManyField(Client, through='Order')
    workers = models.ManyToManyField(Worker, through='Order')

    def __str__(self):
        return self.name


class Order(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    order_date_time = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.food} - {self.ingredient} - {self.client} - {self.worker} - {self.order_date_time}'
