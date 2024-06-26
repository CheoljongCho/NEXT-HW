# Generated by Django 5.0.3 on 2024-04-04 05:54

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0002_article_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='reg_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(choices=[('Hobby', '취미'), ('Food', '음식'), ('Programming', '프로그래밍'), ('none', '기타')], max_length=20),
        ),
    ]