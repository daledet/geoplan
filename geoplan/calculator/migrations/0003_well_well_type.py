# Generated by Django 3.2.7 on 2021-09-06 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0002_well'),
    ]

    operations = [
        migrations.AddField(
            model_name='well',
            name='well_type',
            field=models.CharField(default=False, max_length=30),
        ),
    ]
