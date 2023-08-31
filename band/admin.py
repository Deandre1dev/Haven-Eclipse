from django.contrib import admin
from.models import MusicItem
from.models import TourItem

# Register your models here.
# The models that I created are registered on the admin site.
admin.site.register(MusicItem)

admin.site.register(TourItem)