# Generated by Django 2.0.7 on 2018-07-13 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_event_organizers_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='place',
            field=models.TextField(blank=True, null=True),
        ),
    ]
