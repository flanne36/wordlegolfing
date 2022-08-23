from audioop import reverse
from email.policy import default
from sched import scheduler
from urllib import request
from django.shortcuts import render, redirect
from .models import *
from accounts.models import Profile
import datetime
from django.contrib.auth.decorators import login_required
import json
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
import random



# Create your views here.
@login_required(login_url='login')
def home(request):
    start = datetime.datetime(2022, 8, 1,0,0,0)
    today = datetime.datetime.now()
    todays_index = (today - start).days
    todays_word = NewWordsdata.objects.get(id=todays_index)
    js_data = json.dumps(todays_word.word)
    word_dictionary = Wordsdata.objects.all();
    dictionary = [];
    for word in word_dictionary:
        dictionary.append(word.word)
    js_data2 = json.dumps(dictionary)
    guessed_words = []
    getscores = lookup_score(request.user)
    if getscores is not None:
        if getscores.day == (todays_index - getscores.startday):
            if getscores.guess1 != '':
                guessed_words.append(getscores.guess1)
            if getscores.guess2 != '':
                guessed_words.append(getscores.guess2)
            if getscores.guess3 != '':
                guessed_words.append(getscores.guess3)
            if getscores.guess4 != '':
                guessed_words.append(getscores.guess4)
            if getscores.guess5 != '':
                guessed_words.append(getscores.guess5)
            if getscores.guess6 != '':
                guessed_words.append(getscores.guess6)
        else:
            getscores.guess1 = ''
            getscores.guess2 = ''
            getscores.guess3 = ''
            getscores.guess4 = ''
            getscores.guess5 = ''
            getscores.guess6 = ''
            getscores.save()

    stats = lookup_profile(request.user)
    if stats is None:
        stats = Profile()
        stats.user = request.user
        stats.save()
    played = stats.played
    losses = stats.losses
    if stats.losses == 0:
        percentage = 100
    else:
        percentage = int(((float(played) - float(stats.losses)) / float(played)) * 100)
    curStreak = stats.current_streak
    maxStreak = stats.max_streak
    oneWins = stats.one_wins
    twoWins = stats.two_wins
    threeWins = stats.three_wins
    fourWins = stats.four_wins
    fiveWins = stats.five_wins
    sixWins = stats.six_wins

    context = {
        'todays_word' : js_data,
        'word_dictionary' : js_data2,
        'guessed_words' : guessed_words,
        'played' : played,
        'percentage' : percentage,
        'losses' : losses,
        'curStreak' : curStreak,
        'maxStreak' : maxStreak,
        'oneWins' : oneWins,
        'twoWins' : twoWins,
        'threeWins' : threeWins,
        'fourWins' : fourWins,
        'fiveWins' : fiveWins,
        'sixWins' : sixWins,
    }
    return render(request, 'home.html', context=context)

@csrf_exempt
@login_required(login_url='login')
def stats(request):
    score = request.POST.get('wordCount')
    word = request.POST.get('word')
    word = word.replace('"', '')
    saveScore = lookup_score(request.user)
    start = datetime.datetime(2022, 8, 1,0,0,0)
    today = datetime.datetime.now()
    if saveScore is None:
        saveScore = ScoreBoard()
        saveScore.user = request.user
        saveScore.day = 0
        saveScore.startday = (today - start).days
        saveScore.day1 = int(score) - 4
        saveScore.totalscore = int(score) - 4
        saveScore.guess1 = word
        saveScore.save()
    else:
        day = (today - start).days - saveScore.startday
        if saveScore.guess1 == '':
            saveScore.guess1 = word
        elif saveScore.guess2 == '':
            saveScore.guess2 = word
        elif saveScore.guess3 == '':
            saveScore.guess3 = word
        elif saveScore.guess4 == '':
            saveScore.guess4 = word
        elif saveScore.guess5 == '':
            saveScore.guess5 = word
        elif saveScore.guess6 == '':
            saveScore.guess6 = word

        match day:
            case 0:
                if(int(score)-4 != 0):
                    saveScore.day1 = int(score) - 4
                else:
                    saveScore.day1 = 'E'
                saveScore.totalscore = saveScore.totalscore + int(score) - 4
                saveScore.day = day
                saveScore.save()
            case 1:
                if(int(score)-4 != 0):
                    saveScore.day2 = int(score) - 4
                else:
                    saveScore.day2 = 'E'
                saveScore.totalscore = saveScore.totalscore + int(score) - 4
                saveScore.day = day
                saveScore.save()
            case 2:
                if(int(score)-4 != 0):
                    saveScore.day3 = int(score) - 4
                else:
                    saveScore.day3 = 'E'
                saveScore.totalscore = saveScore.totalscore + int(score) - 4
                saveScore.day = day
                saveScore.save()
            case 3:
                if(int(score)-4 != 0):
                    saveScore.day4 = int(score) - 4
                else:
                    saveScore.day4 = 'E'
                saveScore.totalscore = saveScore.totalscore + int(score) - 4
                saveScore.day = day
                saveScore.save()
            case 4:
                if(int(score)-4 != 0):
                    saveScore.day5 = int(score) - 4
                else:
                    saveScore.day5 = 'E'
                saveScore.totalscore = saveScore.totalscore + int(score) - 4
                saveScore.day = day
                saveScore.save()
            case 5:
                if(int(score)-4 != 0):
                    saveScore.day6 = int(score) - 4
                else:
                    saveScore.day6 = 'E'
                saveScore.totalscore = saveScore.totalscore + int(score) - 4
                saveScore.day = day
                saveScore.save()
            case 6:
                if(int(score)-4 != 0):
                    saveScore.day7 = int(score) - 4
                else:
                    saveScore.day7 = 'E'
                saveScore.totalscore = saveScore.totalscore + int(score) - 4
                saveScore.day = day
                saveScore.save()
            case 7:
                if(int(score)-4 != 0):
                    saveScore.day8 = int(score) - 4
                else:
                    saveScore.day8 = 'E'
                saveScore.totalscore = saveScore.totalscore + int(score) - 4
                saveScore.day = day
                saveScore.save()
            case 8:
                if(int(score)-4 != 0):
                    saveScore.day9 = int(score) - 4
                else:
                    saveScore.day9 = 'E'
                saveScore.totalscore = saveScore.totalscore + int(score) - 4
                saveScore.day = day
                saveScore.save()
            case 9:
                if(int(score)-4 != 0):
                    saveScore.day10 = int(score) - 4
                else:
                    saveScore.day10 = 'E'
                saveScore.totalscore = saveScore.totalscore + int(score) - 4
                saveScore.day = day
                saveScore.save()
            case 10:
                if(int(score)-4 != 0):
                    saveScore.day11 = int(score) - 4
                else:
                    saveScore.day11 = 'E'
                saveScore.totalscore = saveScore.totalscore + int(score) - 4
                saveScore.day = day
                saveScore.save()
            case 11:
                if(int(score)-4 != 0):
                    saveScore.day12 = int(score) - 4
                else:
                    saveScore.day12 = 'E'
                saveScore.totalscore = saveScore.totalscore + int(score) - 4
                saveScore.day = day
                saveScore.save()
            case 12:
                if(int(score)-4 != 0):
                    saveScore.day13 = int(score) - 4
                else:
                    saveScore.day13 = 'E'
                saveScore.totalscore = saveScore.totalscore + int(score) - 4
                saveScore.day = day
                saveScore.save()
            case 13:
                if(int(score)-4 != 0):
                    saveScore.day14 = int(score) - 4
                else:
                    saveScore.day14 = 'E'
                saveScore.totalscore = saveScore.totalscore + int(score) - 4
                saveScore.day = day
                saveScore.save()
            case 14:
                if(int(score)-4 != 0):
                    saveScore.day15 = int(score) - 4
                else:
                    saveScore.day15 = 'E'
                saveScore.totalscore = saveScore.totalscore + int(score) - 4
                saveScore.day = day
                saveScore.save()
            case 15:
                if(int(score)-4 != 0):
                    saveScore.day16 = int(score) - 4
                else:
                    saveScore.day16 = 'E'
                saveScore.totalscore = saveScore.totalscore + int(score) - 4
                saveScore.day = day
                saveScore.save()
            case 16:
                if(int(score)-4 != 0):
                    saveScore.day17 = int(score) - 4
                else:
                    saveScore.day17 = 'E'
                saveScore.totalscore = saveScore.totalscore + int(score) - 4
                saveScore.day = day
                saveScore.save()
            case 17:
                if(int(score)-4 != 0):
                    saveScore.day18 = int(score) - 4
                else:
                    saveScore.day18 = 'E'
                saveScore.totalscore = saveScore.totalscore + int(score) - 4
                saveScore.day = day
                saveScore.save()

    profile = lookup_profile(request.user)
    if profile is None:
        profile = Profile()
        profile.user = request.user
    profile.played = profile.played + 1
    if int(score) > 6:
        profile.losses = profile.losses + 1
        profile.current_streak = 0
    else:
        profile.current_streak = profile.current_streak + 1
        if profile.current_streak > profile.max_streak:
            profile.max_streak = profile.current_streak
        match(int(score)):
            case 1:
                profile.one_wins = profile.one_wins + 1
            case 2:
                profile.two_wins = profile.two_wins + 1
            case 3:
                profile.three_wins = profile.three_wins + 1
            case 4:
                profile.four_wins = profile.four_wins + 1
            case 5:
                profile.five_wins = profile.five_wins + 1
            case 6:
                profile.six_wins = profile.six_wins + 1
            
    profile.save()

    return HttpResponse('OK')


def lookup_score(user):
    try:
        score = ScoreBoard.objects.all().filter(user=user).get()
        return score
    except ObjectDoesNotExist:
        return None

def lookup_profile(user):
    try:
        profile = Profile.objects.all().filter(user=user).get()
        return profile
    except ObjectDoesNotExist:
        return None

@csrf_exempt
@login_required(login_url='login')
def saveguess(request):
    result = request.body
    word = json.loads(result)
    saveguess = lookup_score(request.user)
    start = datetime.datetime(2022, 8, 1,0,0,0)
    today = datetime.datetime.now()
    if saveguess is None:
        saveguess = ScoreBoard()
        saveguess.user = request.user
        saveguess.day = 0
        saveguess.startday = (today - start).days
        saveguess.guess1 = word
        saveguess.save()
    else:
        day = (today - start).days - saveguess.startday
        if day-1 != saveguess.day:
            misseddays = day - 1 - saveguess.day
            for x in range(misseddays):
                inputday = day - 1 - x
                match day:
                    case 1:
                        saveguess.day1 = 4
                        saveguess.totalscore = saveguess.totalscore + 4
                        saveguess.save()
                    case 2:
                        saveguess.day2 = 4
                        saveguess.totalscore = saveguess.totalscore + 4
                        saveguess.save()
                    case 3:
                        saveguess.day3 = 4
                        saveguess.totalscore = saveguess.totalscore + 4
                        saveguess.save()
                    case 4:
                        saveguess.day4 = 4
                        saveguess.totalscore = saveguess.totalscore + 4
                        saveguess.save()
                    case 5:
                        saveguess.day5 = 4
                        saveguess.totalscore = saveguess.totalscore + 4
                        saveguess.save()
                    case 6:
                        saveguess.day6 = 4
                        saveguess.totalscore = saveguess.totalscore + 4
                        saveguess.save()
                    case 7:
                        saveguess.day7 = 4
                        saveguess.totalscore = saveguess.totalscore + 4
                        saveguess.save()
                    case 8:
                        saveguess.day8 = 4
                        saveguess.totalscore = saveguess.totalscore + 4
                        saveguess.save()
                    case 9:
                        saveguess.day9 = 4
                        saveguess.totalscore = saveguess.totalscore + 4
                        saveguess.save()
                    case 10:
                        saveguess.day10 = 4
                        saveguess.totalscore = saveguess.totalscore + 4
                        saveguess.save()
                    case 11:
                        saveguess.day11 = 4
                        saveguess.totalscore = saveguess.totalscore + 4
                        saveguess.save()
                    case 12:
                        saveguess.day12 = 4
                        saveguess.totalscore = saveguess.totalscore + 4
                        saveguess.save()
                    case 13:
                        saveguess.day13 = 4
                        saveguess.totalscore = saveguess.totalscore + 4
                        saveguess.save()
                    case 14:
                        saveguess.day14 = 4
                        saveguess.totalscore = saveguess.totalscore + 4
                        saveguess.save()
                    case 15:
                        saveguess.day15 = 4
                        saveguess.totalscore = saveguess.totalscore + 4
                        saveguess.save()
                    case 16:
                        saveguess.day16 = 4
                        saveguess.totalscore = saveguess.totalscore + 4
                        saveguess.save()
                    case 17:
                        saveguess.day17 = 4
                        saveguess.totalscore = saveguess.totalscore + 4
                        saveguess.save()
        
        saveguess.day = day
        saveguess.save()
        if saveguess.guess1 == '':
            saveguess.guess1 = word
            saveguess.save()
        elif saveguess.guess2 =='':
            saveguess.guess2 = word
            saveguess.save()
        elif saveguess.guess3 == '':
            saveguess.guess3 = word
            saveguess.save()
        elif saveguess.guess4 == '':
            saveguess.guess4 = word
            saveguess.save()
        elif saveguess.guess5 == '':
            saveguess.guess5 = word
            saveguess.save()
        elif saveguess.guess6 == '':
            saveguess.guess6 = word
            saveguess.save()
            
    return HttpResponse('OK')