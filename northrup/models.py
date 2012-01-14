from django.db import models
from mezzanine.core.models import Displayable, RichTextField

class Homepage(Displayable):
    header_top_left = RichTextField(blank=True, verbose_name="Header Top Left")
    header_top_right = RichTextField(blank=True, verbose_name="Header Top Right")
    header_middle_left = RichTextField(blank=True, verbose_name="Header Middle Left")
    header_middle_right = RichTextField(blank=True, verbose_name="Header Middle Right")
    body_left_column_top = RichTextField(blank=True, verbose_name="Body Left Column Top")
    body_left_column_bottom = RichTextField(blank=True, verbose_name="Body Left Column Bottom")
    body_middle_column_top = RichTextField(blank=True, verbose_name="Body Middle Column Top")
    body_middle_column_bottom = RichTextField(blank=True, verbose_name="Body Middle Column Bottom")
    body_right_column = RichTextField(blank=True, verbose_name="Body Left Column Bottom")

    def __unicode__(self):
        return self.title

class Event(models.Model):
    date = models.DateField(verbose_name="Date")
    event = models.CharField(max_length=400, verbose_name="Event")
    location = models.CharField(max_length=400, verbose_name="Location")
    start_time = models.TimeField(verbose_name="Start Time")
    end_time = models.TimeField(verbose_name="End Time")
    
    def __unicode__(self):
        return self.event

