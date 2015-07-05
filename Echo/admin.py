from django.contrib import admin

from Echo.models import *

class IntentsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Intents, IntentsAdmin)

class SlotAdmin(admin.ModelAdmin):
    pass

admin.site.register(Slot, SlotAdmin)
