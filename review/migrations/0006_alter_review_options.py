# Generated by Django 5.1.4 on 2024-12-27 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0005_alter_review_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'verbose_name': '口コミ', 'verbose_name_plural': '口コミ一覧'},
        ),
    ]
