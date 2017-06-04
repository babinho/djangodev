from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Kupac(models.Model):
    ime = models.CharField(max_length=50)
    prezime = models.CharField(max_length=50)

class Vrsta(models.Model):
    vrsta = models.CharField(max_length=50)

class Marka(models.Model):
    marka = models.CharField(max_length=50)

class Status(models.Model):
    status = models.CharField(max_length=50)

class Nalog(models.Model):
    serviser = models.ForeignKey(User)
    kupac = models.ForeignKey(Kupac)
    marka = models.ForeignKey(Marka)
    vrsta = models.ForeignKey(Vrsta)
    dodatno = models.TextField(null=True)
    serijski_br = models.CharField(max_length=50)
    opis_k = models.TextField()
    opis_s = models.TextField()
    pretpostavka_cijene = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True)
    cijena = models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True)
    status = models.ForeignKey(Status)
    odgovor_k = models.TextField(null=True,blank=True)
    upit_k = models.TextField(null=True,blank=True)

class Akcija(models.Model):
    nalog = models.ForeignKey(Nalog)
    akcija = models.TextField()
    cijena = models.DecimalField(max_digits=12, decimal_places=2)
