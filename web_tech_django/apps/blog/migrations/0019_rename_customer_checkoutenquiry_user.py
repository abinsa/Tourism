# Generated by Django 4.0 on 2024-06-01 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_checkoutenquiry_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checkoutenquiry',
            old_name='customer',
            new_name='user',
        ),
    ]