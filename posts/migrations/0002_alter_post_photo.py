# Generated by Django 5.1.5 on 2025-01-19 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(default='posts/default.jpg', max_length=300, upload_to='posts'),
        ),
    ]
