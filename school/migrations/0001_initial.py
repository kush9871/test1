# Generated by Django 3.0.14 on 2022-07-02 04:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stuid', models.IntegerField()),
                ('stuname', models.CharField(max_length=100)),
                ('sturoll', models.IntegerField()),
                ('stumail', models.EmailField(max_length=254)),
                ('stupass', models.CharField(max_length=50)),
                ('datetime', models.DateTimeField(default=datetime.datetime(2022, 7, 2, 10, 5, 38, 749691))),
            ],
        ),
    ]
