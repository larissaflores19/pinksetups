from django.db import models
import datetime
from django.utils import timezone

# Create your models here.


class Pinksetup(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Favorites(models.Model):
    all_text = models.ForeignKey(Pinksetup, on_delete=models.CASCADE)
    favorite_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.favorite_text
