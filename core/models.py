from django.db import models

class HomeImage(models.Model):
    image = models.ImageField()
    background_color = models.CharField(default='#000000', max_length=10)

class Department(models.Model):
    name = models.CharField(max_length=20)
    abbreviation = models.CharField(max_length=10)

class Sponsor(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField()
    website_url = models.CharField(max_length=100, null=True)

class Event(models.Model):
    year = models.PositiveSmallIntegerField()
    date = models.DateField()
    place = models.CharField(max_length=50)
    start_at = models.TimeField()
    end_at = models.TimeField()
    fee = models.PositiveSmallIntegerField()
    after_party_fee = models.PositiveSmallIntegerField()
    early_bird_discount_rate = models.PositiveSmallIntegerField(default=50)
    early_bird_capacity = models.PositiveSmallIntegerField(default=30)
    early_bird_start_at = models.DateTimeField()
    regular_start_at = models.DateTimeField()
    early_bird_form_url = models.CharField(max_length=100, null=True)
    regular_form_url = models.CharField(max_length=100, null=True)
    early_bird_finished = models.BooleanField()
    regular_finished = models.BooleanField()
    timetable = models.TextField()
    theme = models.CharField(max_length=50, null=True)
    theme_explanation = models.CharField(max_length=700, null=True)
    letter_title = models.CharField(max_length=100, null=True)
    letter_text = models.CharField(max_length=1000, null=True)
    sponsors = models.ManyToManyField(Sponsor)

class Organizer(models.Model):
    name = models.CharField(max_length=10)
    event = models.ForeignKey(Event, null=True, on_delete=models.SET_NULL)
    image = models.ImageField()
    department = models.ForeignKey(Department, null=True, on_delete=models.SET_NULL)
    entered_year = models.PositiveSmallIntegerField()

class Speaker(models.Model):
    name = models.CharField(max_length=10)
    event = models.ForeignKey(Event, null=True, on_delete=models.SET_NULL)
    image = models.ImageField()
    explanation = models.CharField(max_length=600, null=True)
    youtube_url = models.CharField(max_length=100, null=True)
    published_datetime = models.DateTimeField()

class Setting(models.Model):
    home_image = models.ForeignKey(HomeImage, null=True, on_delete=models.SET_NULL)
    event_now = models.ForeignKey(Event, null=True, on_delete=models.SET_NULL)