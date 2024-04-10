# Generated by Django 5.0.3 on 2024-04-10 08:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0006_alter_article_category_comment_adcomment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adcomment',
            old_name='content',
            new_name='adcontent',
        ),
        migrations.AlterField(
            model_name='adcomment',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adcomments', to='blogApp.comment'),
        ),
    ]
