# Generated by Django 5.0.4 on 2024-04-29 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_previous_accessed_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='last_accessed_time',
        ),
        migrations.RemoveField(
            model_name='post',
            name='last_accessed_user',
        ),
        migrations.RemoveField(
            model_name='post',
            name='previous_accessed_time',
        ),
        migrations.RemoveField(
            model_name='post',
            name='previous_accessed_user',
        ),
    ]