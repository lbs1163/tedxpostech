from django.db import models
from datetime import date

class HomeImage(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='home_images')
    background_color = models.CharField(default='#000000', max_length=10)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=20)
    abbreviation = models.CharField(max_length=10)

    def __str__(self):
        return self.name + " " + self.abbreviation

class Sponsor(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='sponsors')
    website_url = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    year = models.PositiveSmallIntegerField()
    order = models.PositiveSmallIntegerField()
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
    early_bird_form_url = models.CharField(max_length=100, null=True, blank=True)
    regular_form_url = models.CharField(max_length=100, null=True, blank=True)
    early_bird_finished = models.BooleanField()
    regular_finished = models.BooleanField()
    timetable = models.TextField(null=True, blank=True)
    theme = models.CharField(max_length=50, null=True, blank=True)
    theme_explanation = models.TextField(null=True, blank=True)
    letter_title = models.CharField(max_length=100, null=True, blank=True)
    letter_text = models.TextField(null=True, blank=True)
    letter_end = models.TextField(null=True, blank=True)
    organizers_photo = models.ImageField(null=True, blank=True, upload_to='organizers')
    sponsors = models.ManyToManyField(Sponsor, blank=True)

    def is_end(self):
        return date.today() > self.date

    def __str__(self):
        return str(self.year) + " TEDxPOSTECH"

class Organizer(models.Model):
    name = models.CharField(max_length=10)
    event = models.ForeignKey(Event, null=True, blank=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='organizers')
    department = models.ForeignKey(Department, null=True, blank=True, on_delete=models.SET_NULL)
    entered_year = models.PositiveSmallIntegerField()

    def __str__(self):
        return str(self.event) + " " + self.name

class Speaker(models.Model):
    name = models.CharField(max_length=10)
    event = models.ForeignKey(Event, null=True, blank=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='speakers')
    explanation = models.TextField(null=True, blank=True)
    youtube_url = models.CharField(max_length=100, null=True, blank=True)
    published_datetime = models.DateTimeField()

    def __str__(self):
        return str(self.event) + " " + self.name

class Setting(models.Model):
    home_image = models.ForeignKey(HomeImage, null=True, blank=True, on_delete=models.SET_NULL)
    event_now = models.ForeignKey(Event, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.event_now) + " " + str(self.home_image)