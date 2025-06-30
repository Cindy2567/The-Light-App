from django.contrib import admin
from .models import Sermon, Event, Devotional


class SermonAdmin(admin.ModelAdmin):
    list_display=('title','preacher','date')



# Register your models here.

admin.site.register(Sermon)
admin.site.register(Event)
admin.site.register(Devotional)







