# Generated by Django 5.1.5 on 2025-01-22 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_post_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
