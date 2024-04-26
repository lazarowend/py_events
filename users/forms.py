from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Nome da Tarefa...'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Descrição da Tarefa...'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Senha...'}))

