# Generated by Django 3.0.8 on 2020-08-26 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('clinicid', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('pswd', models.CharField(max_length=20)),
                ('clinicname', models.CharField(max_length=50)),
                ('cityname', models.CharField(max_length=20)),
                ('pincode', models.IntegerField()),
                ('timein', models.TimeField()),
                ('timeout', models.TimeField()),
                ('mobile', models.IntegerField()),
                ('noofdoctors', models.IntegerField()),
            ],
        ),
    ]
