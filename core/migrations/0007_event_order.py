# Generated by Django 2.0.7 on 2018-07-09 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20180709_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='order',
            field=models.PositiveSmallIntegerField(default=4),
            preserve_default=False,
        ),
    ]
