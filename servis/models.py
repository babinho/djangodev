from django.db import models

# Create your models here.

class Nalog(models.Model):
    serviser = models.CharField(max_length=32)