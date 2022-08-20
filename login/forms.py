from email.mime import image
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django import forms
from django.forms import ModelForm

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control",
                "type": "text",
                "placeholder": "Enter firstname"

            }
        )
    )

    last_name = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control",
                "type": "text",
                "placeholder": "Enter Lastname"
            }
        )
    )
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "text",
        "placeholder": "Enter Username"
    }))

    email = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "email",
        "placeholder": "Enter Email-id"
    }))

    image = forms.FileField(
        widget= forms.FileInput(
            attrs={
                "class": "form-control",
                "type": "file",
                

            }
        )
    )

    password1 = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "password",
        "placeholder": "Enter Password"
    }))

    password2 = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "password",
        "placeholder": "Re-enter Password"
    }))
    

    desc = forms.CharField(
        widget= forms.Textarea(
            attrs={
                "class": "form-control",
                "type": "text",
                "placeholder": "Describe Yourself Here... ",
                "rows":"4"

            }
        )
    )

    

    class Meta:
        model = User
        fields = ('first_name','last_name','username', 'email', 'desc', 'password1', 'password2')


class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    password = forms.CharField(
        widget= forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )


