
from django.shortcuts import render, redirect
from django.contrib import messages
from accounts.forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from game.models import ScoreBoard, Wordsdata

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
        render(request, 'accounts/register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('accounts:login')


def scoreboard(request):
    django_scores = ScoreBoard.objects.all()
    scores = []
    for score in django_scores:
        scores.append(
            [score.user.username, score.day1, score.day2, score.day3, score.day4, score.day5, score.day6, score.day7,
             score.day8, score.day9,
             score.day10, score.day11, score.day12, score.day13, score.day14, score.day15, score.day16, score.day17,
             score.day18, score.totalscore])
    context = {
        'scores': scores
    }

    return render(request, 'scoreboard.html', context)