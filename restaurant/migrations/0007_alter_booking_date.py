# Generated by Django 4.2.7 on 2023-12-06 20:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("restaurant", "0006_alter_booking_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="booking",
            name="date",
            field=models.DateField(),
        ),
    ]
