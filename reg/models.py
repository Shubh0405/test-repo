from django.db import models

# Create your models here.

class Registration(models.Model):
    name = models.CharField(max_length=254)
    college = models.CharField(max_length=254)
    number = models.CharField(max_length=254)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=254, unique=True)
    discord = models.CharField(max_length=254,null=True)

    def __str__(self):
        return self.name
