from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here. 

class Product(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Opinion(models.Model):
    #host
    #topic
    # class Products(models.TextChoices):
    #     MALM = "malm"
    #     SODERHAMN = "soderhamn"
    #     PAX = "pax"
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    # _product = models.CharField(
    #     max_length=15, 
    #     choices=Products.choices
        # )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    opinion = models.TextField()
    created = models.DateTimeField(
        auto_now_add=True
        )

    def __str__(self):
        return self.opinion[0:50]

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    opinion = models.ForeignKey(Opinion, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(
        auto_now_add=True
        )
    def __str__(self):
        return self.body[0:50]

