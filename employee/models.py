from django.db import models

class Emp(models.Model):
    name = models.CharField(max_length=50, blank=True, default='')
    role = models.CharField(max_length=50, blank=True, default='')
    exp  = models.IntegerField(max_length=3, blank=True, default=0)
    ts   = models.TextField()