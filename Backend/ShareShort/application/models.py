from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=50 , blank=True)
    about = models.CharField(max_length=300,blank=True)
    profile_image_url = models.CharField(max_length=200,blank=True)
    facebook = models.URLField(max_length=100, blank=True)
    instagram = models.URLField(max_length=100, blank=True)
    twitter = models.URLField(max_length=100, blank=True)
    threads = models.URLField(max_length=100, blank=True)
    telegram = models.URLField(max_length=100, blank=True)
    whatsapp = models.URLField(max_length=100, blank=True)
    youtube = models.URLField(max_length=100, blank=True)
    discord = models.URLField(max_length=100, blank=True)
    github = models.URLField(max_length=100, blank=True)
    linkedin = models.URLField(max_length=100, blank=True)
    snapchat = models.URLField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

class ExtraLinks(models.Model):
    label = models.CharField(max_length=100)
    icon = models.CharField(max_length=15)
    url = models.URLField(max_length=500)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    enabled = models.BooleanField(default=True)
    position = models.IntegerField()


class Store(models.Model):
    url = models.URLField(max_length=500)
    title = models.CharField(max_length=100)
    product_image_url = models.CharField(max_length=200)
    price = models.CharField(max_length=10)
    currency = models.CharField(max_length=5)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    enabled = models.BooleanField(default=True)

