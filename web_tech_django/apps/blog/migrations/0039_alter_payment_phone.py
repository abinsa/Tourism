# Generated by Django 5.0.4 on 2024-07-01 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0038_alter_hotelcheckout_tour_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='phone',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
