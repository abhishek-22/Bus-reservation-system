# Generated by Django 3.0.7 on 2020-06-08 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus',
            name='seats',
            field=models.IntegerField(),
        ),
    ]