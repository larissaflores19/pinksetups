from django.db import models
from django.db.models import TextField, ForeignKey, Model, ImageField, CharField
from django.forms import ChoiceField

VOTE_CHOICE = (
    ("1", "One"),
    ("2", "Two"),
    ("3", "Three"),
    ("4", "Four"),
    ("5", "Five"),
)


class PinkSetup(Model):
    name = CharField(default='', max_length=200)
    description = TextField(blank=True)
    image = ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Favorites(models.Model):
    item = ForeignKey(PinkSetup, on_delete=models.CASCADE)
    comment = TextField(blank=True)
    vote = ChoiceField(choices=VOTE_CHOICE)

    def __str__(self):
        return self.comment

