# Generated by Django 2.2.7 on 2020-03-28 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0004_auto_20200327_2108'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='available_front_page',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='available_front_page',
            field=models.BooleanField(default=True),
        ),
    ]
