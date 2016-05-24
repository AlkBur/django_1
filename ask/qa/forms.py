
from django import forms
from qa.models import Question, Answer
from django.contrib.auth.models import User


class AskForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ['title', 'text']

class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ['text', 'question']

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput, max_length=30)

