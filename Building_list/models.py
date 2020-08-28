from django.db import models
from django.conf import settings

FlAG = [
    ('사용중', '사용중'),
    ('빈강의실', '빈강의실'),
]
WEEK = [
    ('월', '월'),
    ('화', '화'),
    ('수', '수'),
    ('목', '목'),
    ('금', '금'),
    ('토', '토'),
    ('일', '일'),
]
class Lecture(models.Model):
    #호
    number = models.CharField(max_length=10, default='')
    #층
    floor = models.CharField(max_length=10, default='')
    #수업시간(24시 기준)
    class_time = models.CharField(max_length=20, default='')
    #사용가능시간
    available_time = models.CharField(max_length=20, default='')
    #사용여부
    on_off = models.CharField(max_length=50, choices=FlAG, default='빈강의실')
    #요일
    day_of_the_week = models.CharField(max_length=20, choices=WEEK, default='월')

class Building(models.Model):
    #건물이름
    name = models.TextField(max_length=200, default='')
    #강의 모델
    lecture = models.ManyToManyField(Lecture)

class Reservation(models.Model):
    # 강의 모델
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE, related_name="lecture_list")
    # 목적
    purpose = models.TextField(max_length=100, default='')
    # 사용시간
    use_time = models.CharField(max_length=20, default='')
    # 유저모델
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='photos')
