# Generated by Django 3.1.5 on 2021-07-08 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver_side', '0012_auto_20210709_0002'),
    ]

    operations = [
        migrations.AddField(
            model_name='modeldetail',
            name='model',
            field=models.CharField(default=0, max_length=150),
            preserve_default=False,
        ),
    ]