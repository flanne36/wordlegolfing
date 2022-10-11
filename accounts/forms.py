from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput
from game.models import *


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'first_name', 'email', 'password1', 'password2']

class MessageForm(ModelForm):
	class Meta:
		model = Message
		fields = ['message']
		widgets = {
			'message': TextInput(attrs={
				'class':'comment-input',
				'style':'width: 90vw',
				'placeholder':'Add a comment...'
			})
		}