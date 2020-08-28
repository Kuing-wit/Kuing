from django.contrib import admin
from .models import Room, Lecture, Reservation

admin.site.register(Room)
admin.site.register(Lecture)
admin.site.register(Reservation)