# Generated by Django 5.0.4 on 2024-06-05 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0032_rename_people_hotelcheckout_tour_travellers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotelcheckout',
            name='tour_date',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
