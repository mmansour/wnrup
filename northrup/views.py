from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.template import RequestContext
from django.core import serializers
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from django.utils import simplejson
from mezzanine.utils.views import paginate
from northrup.models import Micropage, Event
import logging

logger = logging.getLogger("westernnorthrup.custom")

def home(request):
    try:
        home = get_object_or_404(Micropage, page_type='Home')
        events = Event.objects.all().order_by('-date')
        return render_to_response('index.html',{'home':home, 'events': events,},
                                  context_instance=RequestContext(request))
    except Exception, e:
        logger.error('Error in view: about: {0}'.format(e))
