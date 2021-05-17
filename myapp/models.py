from django.db import models

# Create your models here.
class Crypto(models.Model):
    email = models.CharField(max_length=128,default="")
    telegram_number = models.CharField(max_length=20)
    quotes = models.CharField(max_length=512, default="")
    # def __init__(self):
    #     return self.email