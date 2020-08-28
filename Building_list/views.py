from django.shortcuts import render
from .models import Reservation,Room,Lecture


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
            if (temp.day_of_the_week == day_of_the_week) and (temp.floor == floors):
                room_dict[temp] = i

        return render(request, "Building_list/room_list.html", {"rooms": room_dict})

def room_detail(request, room_id):
    lectures = Lecture.objects.all()
    lecture_dict = {}
    for i in range(0, lectures.__len__()):
        tmp = lectures[i]
        if tmp.room == Room.objects.get(id=room_id):
            lecture_dict[tmp] = i

    return render(request, "Building_list/room_detail.html", {"lectures": lecture_dict})