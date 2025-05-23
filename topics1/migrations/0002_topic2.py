# Generated by Django 5.1.4 on 2024-12-24 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='タイトル')),
                ('description', models.TextField(verbose_name='説明')),
                ('image', models.ImageField(blank=True, null=True, upload_to='topics_images/', verbose_name='画像')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日')),
            ],
        ),
    ]
