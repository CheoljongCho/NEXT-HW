# Generated by Django 5.0.3 on 2024-04-06 10:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_post_duedate'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='duedate',
            field=models.DateField(default=datetime.date.today),
        ),
    ]