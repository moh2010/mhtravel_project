# Generated by Django 2.2.7 on 2020-03-27 12:47

from django.db import migrations, models
import django.db.models.deletion
import tours.models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airline',
            name='airline_code',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='airline',
            name='airline_name',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='airline',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='airline',
            name='slug',
            field=models.SlugField(max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='destination',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='des_city', to='tours.Destination'),
        ),
        migrations.AlterField(
            model_name='city',
            name='slug',
            field=models.SlugField(max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='title',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='destination',
            name='slug',
            field=models.SlugField(max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='destination',
            name='title',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='flight',
            name='airline',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='air_flight', to='tours.Airline'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='arrival_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='flight',
            name='departure_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='flight',
            name='slug',
            field=models.SlugField(max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cit_hotel', to='tours.City'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='destination',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='des_hotel', to='tours.Destination'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='slug',
            field=models.SlugField(max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='stars',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='title',
            field=models.CharField(db_index=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='program',
            name='airline',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='air_programs', to='tours.Airline'),
        ),
        migrations.AlterField(
            model_name='program',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cat_programs', to='tours.Category'),
        ),
        migrations.AlterField(
            model_name='program',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cit_programs', to='tours.City'),
        ),
        migrations.AlterField(
            model_name='program',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='program',
            name='destination',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='des_programs', to='tours.Destination'),
        ),
        migrations.AlterField(
            model_name='program',
            name='district',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='program',
            name='flight',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fly_programs', to='tours.Flight'),
        ),
        migrations.AlterField(
            model_name='program',
            name='hotel_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='htl_programs', to='tours.Hotel'),
        ),
        migrations.AlterField(
            model_name='program',
            name='image_1',
            field=models.ImageField(blank=True, null=True, upload_to=tours.models.program_directory_path),
        ),
        migrations.AlterField(
            model_name='program',
            name='image_2',
            field=models.ImageField(blank=True, null=True, upload_to=tours.models.program_directory_path),
        ),
        migrations.AlterField(
            model_name='program',
            name='image_3',
            field=models.ImageField(blank=True, null=True, upload_to=tours.models.program_directory_path),
        ),
        migrations.AlterField(
            model_name='program',
            name='image_4',
            field=models.ImageField(blank=True, null=True, upload_to=tours.models.program_directory_path),
        ),
        migrations.AlterField(
            model_name='program',
            name='image_5',
            field=models.ImageField(blank=True, null=True, upload_to=tours.models.program_directory_path),
        ),
        migrations.AlterField(
            model_name='program',
            name='image_6',
            field=models.ImageField(blank=True, null=True, upload_to=tours.models.program_directory_path),
        ),
        migrations.AlterField(
            model_name='program',
            name='image_main',
            field=models.ImageField(blank=True, null=True, upload_to=tours.models.program_directory_path),
        ),
        migrations.AlterField(
            model_name='program',
            name='price_adt',
            field=models.DecimalField(decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='program',
            name='price_chd_one',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='program',
            name='price_chd_two',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='program',
            name='price_inf',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='program',
            name='slug',
            field=models.SlugField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='program',
            name='title',
            field=models.CharField(db_index=True, max_length=300, null=True),
        ),
    ]