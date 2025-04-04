# Generated by Django 5.1.4 on 2024-12-19 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='lat',
            field=models.DecimalField(decimal_places=6, max_digits=10, verbose_name='緯度'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='lng',
            field=models.DecimalField(decimal_places=6, max_digits=11, verbose_name='経度'),
        ),
    ]
