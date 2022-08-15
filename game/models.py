
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Wordsdata(models.Model):
    word = models.TextField(null=True)
    id = models.TextField(primary_key=True)


class ScoreBoard(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    startday = models.IntegerField(default=0)
    day = models.IntegerField(default=0)
    guess1 = models.CharField(max_length=5, default='', blank=True)
    guess2 = models.CharField(max_length=5, default='', blank=True)
    guess3 = models.CharField(max_length=5, default='', blank=True)
    guess4 = models.CharField(max_length=5, default='', blank=True)
    guess5 = models.CharField(max_length=5, default='', blank=True)
    guess6 = models.CharField(max_length=5, default='', blank=True)
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

    def __str__(self):
        return self.user.username

