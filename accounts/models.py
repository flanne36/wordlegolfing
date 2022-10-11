from django.db import models

from accounts.views import scoreboard

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    played = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    current_streak = models.IntegerField(default=0)
    max_streak = models.IntegerField(default=0)
    one_wins = models.IntegerField(default=0)
    two_wins = models.IntegerField(default=0)
    three_wins = models.IntegerField(default=0)
    four_wins = models.IntegerField(default=0)
    five_wins = models.IntegerField(default=0)
    six_wins = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username