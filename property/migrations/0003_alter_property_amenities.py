# Generated by Django 3.2.18 on 2023-07-16 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0002_auto_20230716_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='amenities',
            field=models.ManyToManyField(blank=True, to='property.Amenity'),
        ),
    ]
