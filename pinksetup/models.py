from django.db import models
from django.db.models import TextField, ForeignKey, Model, ImageField, CharField
from django.forms import ChoiceField
from django.contrib.auth.models import User
from django.urls import reverse

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


class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    slug = models.SlugField(max_length=250)
    likes = models.ManyToManyField(
        User, related_name="like", default=None, blank=True)

    def get_absolute_url(self):
        return reverse('pinksetup:post_single', args=[self.slug])

    def __str__(self):
        return self.title


