# Generated by Django 2.2 on 2019-04-19 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reg',
            fields=[
                ('user', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('pwd', models.CharField(max_length=20)),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=10)),
                ('dob', models.DateField()),
                ('mobno', models.IntegerField()),
            ],
        ),
    ]
