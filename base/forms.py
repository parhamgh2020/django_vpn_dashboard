from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Message, User

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl'


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': INPUT_CLASSES
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': INPUT_CLASSES
    }))


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('identification_code', 'username', 'email', 'password1', 'password2')

    identification_code = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your identification code',
        'class': INPUT_CLASSES
    }))

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': INPUT_CLASSES
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email address',
        'class': INPUT_CLASSES
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': INPUT_CLASSES
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat password',
        'class': INPUT_CLASSES
    }))


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Your name',
                'class': INPUT_CLASSES
            }),
            'email': forms.TextInput(attrs={
                'placeholder': 'Your email',
                'class': INPUT_CLASSES
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Your message',
                'class': INPUT_CLASSES
            }),
        }
