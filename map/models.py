from django.db import models

class Customer(models.Model):
    name = models.CharField('店舗', max_length=20)
    address = models.CharField('住所', max_length=50)
    lat = models.DecimalField('緯度', max_digits=10, decimal_places=8)
    lng = models.DecimalField('経度', max_digits=11, decimal_places=8)

    def __str__(self):
        return str(self.name)
    class Meta:
        verbose_name = '店舗'
        verbose_name_plural = '店舗'