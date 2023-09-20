from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)


class User(models.Model):
    name = models.CharField(max_length=75)
    products = models.ManyToManyField(Product)


class Lesson(models.Model):
    name = models.CharField(max_length=100)
    link = models.TextField()
    duration = models.IntegerField()
    products = models.ManyToManyField(Product)
    users = models.ManyToManyField(User, through='View')


class View(models.Model):
    lessons = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    view_time = models.PositiveIntegerField()
    status = models.CharField(max_length=15)
