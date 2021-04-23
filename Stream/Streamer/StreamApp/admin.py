from django.contrib import admin

# Register your models here.
from . models import StreamerName,Video
admin.site.register(StreamerName)
admin.site.register(Video)