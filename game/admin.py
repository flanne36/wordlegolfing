from django.contrib import admin
from .models import Wordsdata, ScoreBoard, NewWordsdata

# Register your models here.
admin.site.register(Wordsdata)
admin.site.register(NewWordsdata)
admin.site.register(ScoreBoard)