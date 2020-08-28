from django.shortcuts import render
from .models import Reservation,Room,Lecture
from django.utils import timezone
from datetime import datetime, timedelta, date

def building_list(request):
    return render(request, "Building_list/building_list.html")

def option_check(request):
    return render(request, "Building_list/option_check.html")

def room_list(request):
    if request.method == 'POST':
        day_of_the_week = request.POST['day_of_the_week']
        floors = request.POST['floor']

        rooms = Room.objects.all()
        lectures = Lecture.objects.all()

        room_dict = {}

        for i in range(0, rooms.__len__()):
            temp = rooms[i]
            if ((temp.day_of_the_week == day_of_the_week) and (temp.floor == floors)) or ((temp.day_of_the_week == day_of_the_week) and ('all' == floors)):
                room_dict[temp] = i
                flag = 'true'
                for j in range(0, lectures.__len__()):
                    temp2 = lectures[j]
                    if (temp2.room == temp) and temp2.created_string() != 'false':
                        if flag == 'true':
                            temp.available_time = temp2.start_time
                            temp.name = temp2.name
                            temp.save()
                            flag = 'false'
                        else:
                            time = datetime.combine(date.min, temp.available_time) - datetime.combine(date.min, temp2.start_time)
                            if time > timedelta(minutes=1):
                                temp.available_time = temp2.start_time
                                temp.name = temp2.name
                                temp.save()

        return render(request, "Building_list/room_list.html", {"rooms": room_dict})

def room_detail(request, room_id):
    # lectures = Lecture.objects.all()
    # lecture_dict = {}
    # for i in range(0, lectures.__len__()):
    #     tmp = lectures[i]
    #     if tmp.room == Room.objects.get(id=room_id):
    #         lecture_dict[tmp] = i
    room = Room.objects.get(id=room_id)
    return render(request, "Building_list/room_detail.html", {"room": room})