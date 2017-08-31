from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class UserProfile(models.Model):
    user = models.OneToOneField(User)


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)


class MenuItem(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField(default=0)


class Order(models.Model):
    customer = models.ForeignKey(UserProfile)
    menu_item = models.ManyToManyField(MenuItem, through='OrderDetail')


class OrderDetail(models.Model):
    item = models.ForeignKey(MenuItem)
    order = models.ForeignKey(Order)
    quantity = models.IntegerField()
