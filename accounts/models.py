from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=10, )

    def __str__(self):
        return self.name


class Person(models.Model):
    # Country - Person = 1 : N 관계
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=10, )

    def __str__(self):
        return self.name


class Pet(models.Model):
    # Person - Pet =  1 : N 관계
    person = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=10, )

    def __str__(self):
        return self.name
