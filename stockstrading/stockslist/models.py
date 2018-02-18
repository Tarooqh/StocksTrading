from django.db import models
from django.urls import reverse

# Create your models here.

class Stocksdetail(models.Model):
    index = models.BigIntegerField(blank=True, primary_key=True)
    date = models.TextField(blank=True, null=True)
    symbol = models.TextField(blank=True, null=True)
    open = models.FloatField(blank=True, null=True)
    close = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.symbol

    class Meta:
        managed = False
        db_table = 'stocksdetail'


class Stockslist(models.Model):
    index = models.BigIntegerField(blank=True,primary_key=True)
    symbol = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    marketcap = models.FloatField(blank=True, null=True)
    sector = models.TextField(blank=True, null=True)
    industry = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name + '' + self.symbol

    class Meta:
        managed = False
        db_table = 'stockslist'

    def get_absolute_url(self):
        return reverse("stocks:rtdata", kwargs={"symbol": self.symbol})