# Generated by Django 5.1.4 on 2024-12-27 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0004_alter_review_girl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='comment',
            field=models.TextField(verbose_name='コメント'),
        ),
    ]
