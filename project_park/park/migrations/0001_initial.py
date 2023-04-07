# Generated by Django 4.1.7 on 2023-04-07 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=50)),
                ('vehicle_name', models.CharField(max_length=20)),
                ('registration_no', models.CharField(max_length=10)),
                ('parking_slot', models.CharField(max_length=50)),
                ('occupied_time', models.DateTimeField()),
                ('left_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='ParkingSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('is_available', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=50)),
                ('vehicle_name', models.CharField(max_length=20)),
                ('registration_no', models.CharField(max_length=10)),
                ('occupied_time', models.DateTimeField(auto_now_add=True)),
                ('parking_fees', models.IntegerField()),
                ('parking_slot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='park.parkingslot')),
            ],
        ),
    ]
