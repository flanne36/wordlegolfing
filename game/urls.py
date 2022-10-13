from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('stats/', views.stats, name='stats'),
    path('saveguess/', views.saveguess, name='saveguess'),
    path('test/', views.test, name='test')
]