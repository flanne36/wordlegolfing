from audioop import reverse
from email.policy import default
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

# Create your views here.
@login_required(login_url='login')
def home(request):
    start = datetime.datetime(2022, 8, 1,0,0,0)
    today = datetime.datetime.now()
    todays_index = (today - start).days
    todays_word = Wordsdata.objects.get(id=todays_index)
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
                saveScore.day1 = int(score) - 4
                saveScore.totalscore = saveScore.totalscore + saveScore.day1
                saveScore.day = day
                saveScore.save()
            case 1:
                saveScore.day2 = int(score) - 4
                saveScore.totalscore = saveScore.totalscore + int(saveScore.day2)
                saveScore.day = day
                saveScore.save()
            case 2:
                saveScore.day3 = int(score) - 4
                saveScore.totalscore = saveScore.totalscore + int(saveScore.day3)
                saveScore.day = day
                saveScore.save()
            case 3:
                saveScore.day4 = int(score) - 4
                saveScore.totalscore = saveScore.totalscore + int(saveScore.day4)
                saveScore.day = day
                saveScore.save()
            case 4:
                saveScore.day5 = int(score) - 4
                saveScore.totalscore = saveScore.totalscore + int(saveScore.day5)
                saveScore.day = day
                saveScore.save()
            case 5:
                saveScore.day6 = int(score) - 4
                saveScore.totalscore = saveScore.totalscore + int(saveScore.day6)
                saveScore.day = day
                saveScore.save()
            case 6:
                saveScore.day7 = int(score) - 4
                saveScore.totalscore = saveScore.totalscore + int(saveScore.day7)
                saveScore.day = day
                saveScore.save()
            case 7:
                saveScore.day8 = int(score) - 4
                saveScore.totalscore = saveScore.totalscore + int(saveScore.day8)
                saveScore.day = day
                saveScore.save()
            case 8:
                saveScore.day9 = int(score) - 4
                saveScore.totalscore = saveScore.totalscore + int(saveScore.day9)
                saveScore.day = day
                saveScore.save()
            case 9:
                saveScore.day10 = int(score) - 4
                saveScore.totalscore = saveScore.totalscore + int(saveScore.day10)
                saveScore.day = day
                saveScore.save()
            case 10:
                saveScore.day11 = int(score) - 4
                saveScore.totalscore = saveScore.totalscore + int(saveScore.day11)
                saveScore.day = day
                saveScore.save()
            case 11:
                saveScore.day12 = int(score) - 4
                saveScore.totalscore = saveScore.totalscore + int(saveScore.day12)
                saveScore.day = day
                saveScore.save()
            case 12:
                saveScore.day13 = int(score) - 4
                saveScore.totalscore = saveScore.totalscore + int(saveScore.day13)
                saveScore.day = day
                saveScore.save()
            case 13:
                saveScore.day14 = int(score) - 4
                saveScore.totalscore = saveScore.totalscore + int(saveScore.day14)
                saveScore.day = day
                saveScore.save()
            case 14:
                saveScore.day15 = int(score) - 4
                saveScore.totalscore = saveScore.totalscore + int(saveScore.day15)
                saveScore.day = day
                saveScore.save()
            case 15:
                saveScore.day16 = int(score) - 4
                saveScore.totalscore = saveScore.totalscore + int(saveScore.day16)
                saveScore.day = day
                saveScore.save()
            case 16:
                saveScore.day17 = int(score) - 4
                saveScore.totalscore = saveScore.totalscore + int(saveScore.day17)
                saveScore.day = day
                saveScore.save()
            case 17:
                saveScore.day18 = int(score) - 4
                saveScore.totalscore = saveScore.totalscore + int(saveScore.day18)
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
        saveguess.day = (today - start).days - saveguess.startday
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