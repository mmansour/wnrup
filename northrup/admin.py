from northrup.models import Event
from django.contrib import admin
from mezzanine.core.admin import DisplayableAdmin

class EventAdmin(admin.ModelAdmin):
    class Media:
        js = ("/static/js/MyDateTimeShortcuts.js",)

admin.site.register(Event, EventAdmin)

#class ChoiceInline(admin.TabularInline):
#    model = Choice
#    extra = 2

#class BattleAdmin(DisplayableAdmin):
#
##    fieldsets = battles_fieldsets
#    fieldsets = [
#        ("Title",               {'fields': ['title']}),
#        ("Thumbnail",               {'fields': ['video_thumbnail']}),
#        ("Cast Members",               {'fields': ['cast_members']}),
#        ("Published Date",               {'fields': ['publish_date']}),
#        ("Published Status",               {'fields': ['status']}),
#        ("Type of Video",               {'fields': ['is_homepage', 'is_featured', 'is_bts', 'is_facts', 'is_other']}),
#        ("Video URL",               {'fields': ['video', 'video_youtube_id']}),
#        ("Video Subnav Links",               {'fields': ['bts_link', 'facts_link']}),
#        ("Facts",               {'fields': ['facts']}),
#        ("Poll Question",               {'fields': ['question']}),
#    ]
#
#    inlines = [ChoiceInline]
#    list_display = ('title', 'status', 'is_homepage', 'is_featured', 'is_bts', 'is_facts', 'is_other', 'question', 'publish_date',)
#    list_editable = ('status','is_homepage', 'is_featured', 'is_bts', 'is_facts', 'is_other')
#    list_filter = ['status','publish_date', 'is_featured', 'is_homepage']
#    search_fields = ['title','question']
#    date_hierarchy = 'publish_date'

#class AboutAdmin(DisplayableAdmin):
#    #    fieldsets = battles_fieldsets
#    fieldsets = [
#        ("Title",               {'fields': ['title']}),
#        ("Published Date",               {'fields': ['publish_date']}),
#        ("Published Status",               {'fields': ['status']}),
#        ("About",               {'fields': ['about']}),
#    ]
#
#    list_display = ('title', 'status', 'publish_date',)


#admin.site.register(Battle, BattleAdmin)
#admin.site.register(CastMember)
#admin.site.register(AboutPage, AboutAdmin)
  