# Generated by Django 4.1 on 2022-10-01 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_profile_losses'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='scoreboard_name',
            field=models.TextField(default='t', max_length=50),
        ),
    ]
