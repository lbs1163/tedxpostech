# Generated by Django 2.0.7 on 2018-07-09 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20180709_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='sponsors',
            field=models.ManyToManyField(blank=True, to='core.Sponsor'),
        ),
    ]
