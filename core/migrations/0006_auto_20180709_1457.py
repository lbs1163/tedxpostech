# Generated by Django 2.0.7 on 2018-07-09 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20180709_1304'),
    ]

    operations = [
        migrations.AddField(
            model_name='homeimage',
            name='name',
            field=models.CharField(default='nothing', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='homeimage',
            name='image',
            field=models.ImageField(upload_to='home_images'),
        ),
        migrations.AlterField(
            model_name='organizer',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Department'),
        ),
        migrations.AlterField(
            model_name='organizer',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Event'),
        ),
        migrations.AlterField(
            model_name='organizer',
            name='image',
            field=models.ImageField(upload_to='organizers'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='event_now',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Event'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='home_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.HomeImage'),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Event'),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='image',
            field=models.ImageField(upload_to='speakers'),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='image',
            field=models.ImageField(upload_to='sponsors'),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='website_url',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
