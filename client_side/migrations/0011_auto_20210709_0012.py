# Generated by Django 3.1.5 on 2021-07-08 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client_side', '0010_auto_20210116_0400'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ride',
            old_name='car_id',
            new_name='car_number',
        ),
        migrations.RenameField(
            model_name='ride',
            old_name='order',
            new_name='order_id',
        ),
    ]
