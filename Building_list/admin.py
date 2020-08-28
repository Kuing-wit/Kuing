from django.contrib import admin
from .models import Building, Lecture, Reservation

admin.site.register(Building)
admin.site.register(Lecture)
admin.site.register(Reservation)
