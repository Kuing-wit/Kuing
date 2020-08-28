from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import *

app_name = "Building_list"
urlpatterns = [
    path('', building_list, name='building_list'),
    path('option_check/', option_check, name='option_check'),
    path('room_list/', room_list, name='room_list'),
    path('room_detail/<int:room_id>/', room_detail, name='room_detail'),
]