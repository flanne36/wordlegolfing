from audioop import reverse
from email.policy import default
from urllib import request
from django.shortcuts import render, redirect
from .models import *
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

    context = {
        'todays_word' : js_data,
        'word_dictionary' : js_data2,
        'guessed_words' : guessed_words,
    }
    return render(request, 'home.html', context=context)

@csrf_exempt
@login_required(login_url='login')
def stats(request):
    result = request.body
    score = json.loads(result)
    saveScore = lookup_score(request.user)
    start = datetime.datetime(2022, 8, 1,0,0,0)
    today = datetime.datetime.now()
    if saveScore is None:
        saveScore = ScoreBoard()
        saveScore.user = request.user
        saveScore.day = (today - start).days
        saveScore.day1 = int(score) - 4
        saveScore.totalscore = int(score) - 4
        saveScore.save()
    else:
        day = saveScore.day
        print(day)
        match day:
            case 0:
                print('test')
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

    return HttpResponse('OK')


def lookup_score(user):
    try:
        score = ScoreBoard.objects.all().filter(user=user).get()
        return score
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