# Generated by Django 3.2.18 on 2023-07-22 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_alter_booking_booking_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='number_of_guests',
            field=models.IntegerField(default=0),
        ),
    ]
