# Generated by Django 4.2.8 on 2023-12-07 00:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("restaurant", "0009_alter_booking_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="booking",
            name="date",
            field=models.DateTimeField(),
        ),
    ]
