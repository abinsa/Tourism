# Generated by Django 5.0.4 on 2024-06-08 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0036_alter_hotelcheckout_tour_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='phone',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
