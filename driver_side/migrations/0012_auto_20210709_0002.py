# Generated by Django 3.1.5 on 2021-07-08 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('driver_side', '0011_merge_20210708_2338'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='model_details',
            new_name='model',
        ),
        migrations.RemoveField(
            model_name='car',
            name='model_name',
        ),
    ]
