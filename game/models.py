from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.core.validators import int_list_validator


# Create your models here.
class Wordsdata(models.Model):
    word = models.TextField(null=True)
    id = models.TextField(primary_key=True)


class ScoreBoard(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    startday = models.IntegerField(default=0)
    totalscore = models.IntegerField(default=0)
    day1 = models.CharField(default='-', max_length=5)
    day2 = models.CharField(default='-', max_length=5)
    day3 = models.CharField(default='-', max_length=5)
    day4 = models.CharField(default='-', max_length=5)
    day5 = models.CharField(default='-', max_length=5)
    day6 = models.CharField(default='-', max_length=5)
    day7 = models.CharField(default='-', max_length=5)
    day8 = models.CharField(default='-', max_length=5)
    day9 = models.CharField(default='-', max_length=5)
    day10 = models.CharField(default='-', max_length=5)
    day11 = models.CharField(default='-', max_length=5)
    day12 = models.CharField(default='-', max_length=5)
    day13 = models.CharField(default='-', max_length=5)
    day14 = models.CharField(default='-', max_length=5)
    day15 = models.CharField(default='-', max_length=5)
    day16 = models.CharField(default='-', max_length=5)
    day17 = models.CharField(default='-', max_length=5)
    day18 = models.CharField(default='-', max_length=5)

    # day1 = models.IntegerField(default=0)
    # day2 = models.IntegerField(default=0)
    # day3 = models.IntegerField(default=0)
    # day4 = models.IntegerField(default=0)
    # day5 = models.IntegerField(default=0)
    # day6 = models.IntegerField(default=0)
    # day7 = models.IntegerField(default=0)
    # day8 = models.IntegerField(default=0)
    # day9 = models.IntegerField(default=0)
    # day10 = models.IntegerField(default=0)
    # day11 = models.IntegerField(default=0)
    # day12 = models.IntegerField(default=0)
    # day13 = models.IntegerField(default=0)
    # day14 = models.IntegerField(default=0)
    # day15 = models.IntegerField(default=0)
    # day16 = models.IntegerField(default=0)
    # day17 = models.IntegerField(default=0)
    # day18 = models.IntegerField(default=0)

