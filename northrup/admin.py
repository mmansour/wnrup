from northrup.models import Micropage, Event
from django.contrib import admin
from mezzanine.core.admin import DisplayableAdmin

class MicropageAdmin(DisplayableAdmin):

    fieldsets = [
        ("Title",               {'fields': ['title']}),
        ("Published Date",               {'fields': ['publish_date']}),
        ("Published Status",               {'fields': ['status']}),
        ("Header",               {'fields': ['header_top_left', 'header_top_right','header_middle_left', 'header_middle_right']}),
        ("Body",               {'fields': ['body_left_column_top', 'body_left_column_bottom','body_middle_column_top', 'body_middle_column_bottom','body_right_column']}),
    ]

    list_display = ('title', 'status', 'publish_date',)

class EventAdmin(admin.ModelAdmin):
    pass

admin.site.register(Micropage, MicropageAdmin)
admin.site.register(Event, EventAdmin)

