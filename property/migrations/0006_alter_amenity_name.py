# Generated by Django 3.2.18 on 2023-07-29 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0005_rename_feature_property_is_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amenity',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
