# Generated by Django 4.0.2 on 2022-02-06 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fabi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fabonacci',
            name='numstr',
            field=models.CharField(max_length=20),
        ),
    ]
