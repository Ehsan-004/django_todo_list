# Generated by Django 5.0.2 on 2024-06-22 11:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0004_alter_task_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2024, 6, 22, 14, 52, 47, 482087)),
        ),
    ]
