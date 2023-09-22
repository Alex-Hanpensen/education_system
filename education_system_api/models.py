from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=75)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(max_length=100)
    link = models.TextField()
    duration = models.IntegerField()
    products = models.ManyToManyField(Product)
    users = models.ManyToManyField(User, through='View')

    def __str__(self):
        return self.name


class View(models.Model):
    lessons = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    view_time = models.PositiveIntegerField()
    status = models.CharField(max_length=15)

    def __str__(self):
        return self.status
