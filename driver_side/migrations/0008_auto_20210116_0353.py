# Generated by Django 3.1.5 on 2021-01-15 23:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('driver_side', '0007_auto_20210116_0342'),
    ]

    operations = [
        migrations.RenameField(
            model_name='availablecar',
            old_name='driver_id',
            new_name='driver',
        ),
    ]
