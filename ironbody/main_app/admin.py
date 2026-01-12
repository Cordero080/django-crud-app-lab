from django.contrib import admin
from .models import Workout, Exercise, Equipment

# Register models so they appear in admin panel
admin.site.register(Workout)
admin.site.register(Exercise)
admin.site.register(Equipment)