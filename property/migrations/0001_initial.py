# Generated by Django 3.2.18 on 2023-07-16 10:19

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Amenity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Amenities',
            },
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=80)),
                ('city', models.CharField(max_length=40)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('single_beds', models.IntegerField()),
                ('double_beds', models.IntegerField()),
                ('rooms', models.IntegerField()),
                ('suites', models.IntegerField()),
                ('bathrooms', models.IntegerField()),
                ('is_available', models.BooleanField(default=True)),
                ('price_per_night', models.DecimalField(decimal_places=2, max_digits=6)),
                ('feature', models.BooleanField(default=False)),
                ('featured_image', models.ImageField(upload_to='')),
                ('amenities', models.ManyToManyField(to='property.Amenity')),
            ],
            options={
                'verbose_name_plural': 'Properties',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery', to='property.property')),
            ],
        ),
    ]
