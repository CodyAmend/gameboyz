# Generated by Django 2.1 on 2018-10-15 23:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_order_phonenumber'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='phonenumber',
            new_name='phone_number',
        ),
    ]
