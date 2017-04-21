# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Stock(models.Model):
    ticker = models.CharField(max_length=200)
    close = models.FloatField()
    volume = models.IntegerField()

    def __str__(self):
        return self.ticker
# Create your models here.
