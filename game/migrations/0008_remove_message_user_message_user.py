# Generated by Django 4.1 on 2022-10-07 18:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('game', '0007_remove_message_user_message_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='user',
        ),
        migrations.AddField(
            model_name='message',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
