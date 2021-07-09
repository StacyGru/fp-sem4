# Generated by Django 3.1.5 on 2021-01-15 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=150)),
                ('area', models.CharField(choices=[('центральный', 'центральный'), ('северный', 'северный'), ('южный', 'южный'), ('восточный', 'восточный'), ('западный', 'западный')], max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gearbox', models.CharField(max_length=15)),
                ('body', models.CharField(max_length=15)),
                ('seats', models.PositiveSmallIntegerField()),
                ('drive', models.CharField(max_length=10)),
                ('engine', models.CharField(max_length=10)),
                ('doors', models.PositiveSmallIntegerField()),
                ('rudder', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=15)),
                ('gender', models.CharField(choices=[('Ж', 'женский'), ('М', 'мужской')], max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=150)),
                ('model_name', models.CharField(max_length=150)),
                ('number', models.PositiveIntegerField()),
                ('color', models.CharField(max_length=50)),
                ('model_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='driver_side.carmodel')),
            ],
        ),
        migrations.CreateModel(
            name='AvailableCar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='driver_side.car')),
                ('driver_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='driver_side.driver')),
                ('street_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='driver_side.area')),
            ],
        ),
    ]
