
from django.shortcuts import render, redirect
from django.contrib import messages
from accounts.forms import CreateUserForm, MessageForm
from django.contrib.auth import authenticate, login, logout
from game.models import ScoreBoard, Wordsdata, Message
import datetime


def test(request):
    return render(request, 'scoreboard.html')

# Create your views here.
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')
        context = {}
        return render(request, 'accounts/login.html', context)


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('accounts:login')

        context = {'form': form}
        return render(request, 'accounts/register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('accounts:login')


def scoreboard(request):
    django_scores = ScoreBoard.objects.all().order_by('totalscore')
    scores = []
    standing = "1"
    for score in django_scores:
        scores.append(
            [standing, score.totalscore if score.totalscore != 0 else 'E', score.user.first_name, score.day1, score.day2, score.day3, score.day4, score.day5, score.day6, score.day7,
             score.day8, score.day9,
             score.day10, score.day11, score.day12, score.day13, score.day14, score.day15, score.day16, score.day17,
             score.day18])
        standing = str(int(standing) + 1)
    # for score in scores:
    #     if score[0] == '1':
    #         score[0] = score[0] + 'st'
    #     elif score[0] == '2':
    #         score[0] = score[0] + 'nd'
    #     elif score[0] == '3':
    #         score[0] = score[0] + 'rd'
    #     else:
    #         score[0] = score[0] + 'th'
    chatmessages = Message.objects.all().order_by("-id")
    for score in scores:
        for scoretwo in scores:
            if score[1] == scoretwo[1] and score[2] != scoretwo[2]:
                if "T" not in score[0]:
                    score[0] = score[0] + "T"
                scoretwo[0] = score[0]
    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            newMessage = Message()
            newMessage.user = request.user
            newMessage.message = form.cleaned_data['message']
            newMessage.save()

    context = {
        'scores': scores,
        'messages' : chatmessages,
        'form' : form
    }

    return render(request, 'scoreboard.html', context)