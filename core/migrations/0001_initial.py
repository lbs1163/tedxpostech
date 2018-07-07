# Generated by Django 2.0.7 on 2018-07-07 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('abbreviation', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveSmallIntegerField()),
                ('date', models.DateField()),
                ('place', models.CharField(max_length=50)),
                ('start_at', models.TimeField()),
                ('end_at', models.TimeField()),
                ('fee', models.PositiveSmallIntegerField()),
                ('after_party_fee', models.PositiveSmallIntegerField()),
                ('early_bird_discount_rate', models.PositiveSmallIntegerField(default=50)),
                ('early_bird_capacity', models.PositiveSmallIntegerField(default=30)),
                ('early_bird_start_at', models.DateTimeField()),
                ('regular_start_at', models.DateTimeField()),
                ('early_bird_form_url', models.CharField(max_length=100, null=True)),
                ('regular_form_url', models.CharField(max_length=100, null=True)),
                ('early_bird_finished', models.BooleanField()),
                ('regular_finished', models.BooleanField()),
                ('timetable', models.TextField()),
                ('theme', models.CharField(max_length=50, null=True)),
                ('theme_explanation', models.CharField(max_length=700, null=True)),
                ('letter_title', models.CharField(max_length=100, null=True)),
                ('letter_text', models.CharField(max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HomeImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('background_color', models.CharField(default='#000000', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('image', models.ImageField(upload_to='')),
                ('entered_year', models.PositiveSmallIntegerField()),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Department')),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_now', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Event')),
                ('home_image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.HomeImage')),
            ],
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('image', models.ImageField(upload_to='')),
                ('explanation', models.CharField(max_length=600, null=True)),
                ('youtube_url', models.CharField(max_length=100, null=True)),
                ('published_datetime', models.DateTimeField()),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='')),
                ('website_url', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='sponsors',
            field=models.ManyToManyField(to='core.Sponsor'),
        ),
    ]
