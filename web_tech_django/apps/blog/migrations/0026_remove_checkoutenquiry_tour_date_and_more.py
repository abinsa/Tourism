# Generated by Django 4.0 on 2024-06-02 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_checkoutenquiry_tour_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkoutenquiry',
            name='tour_date',
        ),
        migrations.RemoveField(
            model_name='checkoutenquiry',
            name='tour_travellers',
        ),
    ]
