# Generated by Django 5.1.4 on 2025-04-10 03:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0005_alter_therapist_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='therapist',
            name='schedule',
        ),
        migrations.CreateModel(
            name='WorkSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='出勤日')),
                ('therapist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='list.therapist')),
            ],
        ),
    ]
