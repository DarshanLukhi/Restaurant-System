# Generated by Django 2.0.2 on 2018-03-11 10:34

import BookTable.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='booktable',
            fields=[
                ('id', models.CharField(default=BookTable.models.genrate, editable=False, max_length=20, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=50)),
                ('people', models.IntegerField()),
            ],
        ),
    ]
