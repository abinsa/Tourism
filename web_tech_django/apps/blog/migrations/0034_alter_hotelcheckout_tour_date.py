# Generated by Django 5.0.4 on 2024-06-05 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0033_alter_hotelcheckout_tour_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotelcheckout',
            name='tour_date',
            field=models.DateField(null=True),
        ),
    ]
