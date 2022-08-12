from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.scoreboard, name='scoreboard'),
    path('register/', views.registerPage, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    # path('scoreboard/', views.scoreboard, name='scoreboard'),
]