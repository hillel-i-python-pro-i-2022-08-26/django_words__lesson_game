from django.db import models


class Word(models.Model):
    word = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.word

    __repr__ = __str__


class User(models.Model):
    name = models.CharField(max_length=50)
