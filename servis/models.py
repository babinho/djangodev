from django.db import models


class DummyTable(models.Model):
    ime = models.CharField(max_length=50)
