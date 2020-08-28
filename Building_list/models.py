from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import datetime, timedelta, date

FlAG = [
    ('사용중', '사용중'),
    ('빈강의실', '빈강의실'),
]
WEEK = [ #첫번재가 장고, 두번째가 탬플릿
    ('mon', '월'),
    ('tue', '화'),
    ('wed', '수'),
    ('thu', '목'),
    ('fri', '금'),
]
class Room(models.Model):
    # 호
    number = models.CharField(max_length=10, default='')
    # 사용여부
    on_off = models.CharField(max_length=50, choices=FlAG, default='빈강의실')
    #요일
    day_of_the_week = models.CharField(max_length=20, choices=WEEK, default='월')
    #사용 가능 시간
    available_time = models.TimeField(default='')
    #가장 가까운 강의 이름
    name = models.TextField(max_length=100, default='')
    #층
    floor = models.TextField(max_length=10, default='')

    def __str__(self):
        return self.number+"호/ "+self.day_of_the_week+ "요일"

    def created_string(self):
        time_now = timezone.now().time()

        time = datetime.combine(date.min, self.available_time)-datetime.combine(date.min, time_now)
        if time < timedelta(minutes=1):
            return '수업 없음'
        elif time < timedelta(hours=1):
            return str(int(time.seconds / 60)) + '분'
        elif time < timedelta(days=1):
            return str(int(time.seconds / 3600)) + '시간'
        else:
            return '수업 없음'

class Lecture(models.Model):
    # 룸 모델
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="lecture_room")
    # 강의 명
    name = models.TextField(max_length=100, default='')
    #수업 시작 시간
    start_time = models.TimeField(default='')
    #수업 종료 시간
    finish_time = models.TimeField(default='')

    def __str__(self):
        return self.name

    def created_string(self):
        time_now = timezone.now().time()

        time = datetime.combine(date.min, self.start_time)-datetime.combine(date.min, time_now)
        if time < timedelta(minutes=1):
            return 'false'
        elif time < timedelta(hours=1):
            return str(int(time.seconds / 60)) + '분'
        elif time < timedelta(days=1):
            return str(int(time.seconds / 3600)) + '시간'
        else:
            return 'false'

class Reservation(models.Model):
    # 룸 모델
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="reservation_room")
    # 강의 명
    purpose = models.TextField(max_length=100, default='')
    #예약 시작 시간
    start_time = models.TimeField(default='')
    #예약 종료 시간
    finish_time = models.TimeField(default='')
    #층
    floor = models.TextField(max_length=10, default='')

    def __str__(self):
        return self.name