# Generated by Django 2.2.7 on 2019-12-15 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='price_inf',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
