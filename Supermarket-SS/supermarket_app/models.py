from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    def Integer(self):
        return self.user.id

class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    product_type = models.TextField()
    product_category = models.TextField()
    price = models.IntegerField(default = 0)
    quantity = models.IntegerField(default = 0)
    image = models.ImageField(upload_to='product_images/', verbose_name=_("Image"), null=True, blank=True) 



