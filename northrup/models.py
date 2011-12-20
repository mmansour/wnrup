from django.db import models
from mezzanine.core.models import Displayable, RichTextField

class Event(models.Model):
    date = models.DateField(verbose_name="Date")
    event = models.CharField(max_length=400, verbose_name="Event")
    location = models.CharField(max_length=400, verbose_name="Location")
    start_time = models.TimeField(verbose_name="Start Time")
    end_time = models.TimeField(verbose_name="End Time")
    
    def __unicode__(self):
        return self.event

