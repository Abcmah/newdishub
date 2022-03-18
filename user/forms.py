from dataclasses import fields
from logging import PlaceHolder
from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm

class Sign_up_form(UserCreationForm):
    class Meta:
        model = User
        fields=['first_name','last_name','town','institution','level','username','email','password1','password2']
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control sasa','PlaceHolder':'username'}),
            'first_name':forms.TextInput(attrs={'class':'form-control sasa','PlaceHolder':'First Name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control sasa','PlaceHolder':'Last Name'}),
            'institution':forms.TextInput(attrs={'class':'form-control sasa','PlaceHolder':'institution'}),
            'town':forms.TextInput(attrs={'class':'form-control sasa','PlaceHolder':'city/town'}),
            'level':forms.TextInput(attrs={'class':'form-control sasa','PlaceHolder':'level'}),
            'email':forms.EmailInput(attrs={'class':'form-control sasa','PlaceHolder':'Email'}),
            'password1':forms.TextInput(attrs={'class':'form-control','PlaceHolder':'..................'}),
            'password2':forms.PasswordInput(attrs={'class':'form-control'}),
        }

class Text_post_form(ModelForm):
    class Meta:
        model = Text_post
        fields='__all__'

class Photo_post_form(ModelForm):
    class Meta:
        model = Photo_post
        fields =['photo','text']

class Profile_form(ModelForm):
    class Meta:
        model = User
        fields = ['email','first_name','last_name','level','institution','dp','bio']
        widgets={
        'username':forms.TextInput(attrs={"class":"form-control sasa","PlaceHolder":"username"}),
        'email':forms.TextInput(attrs={'class':'sasa form-control',"PlaceHolder":"Email"}),
        'first_name':forms.TextInput(attrs={'class':'sasa form-control',"PlaceHolder":"First Name"}),
        'last_name':forms.TextInput(attrs={'class':'sasa form-control',"PlaceHolder":"Last Name"}),
        'level':forms.TextInput(attrs={'class':'sasa form-control',"PlaceHolder":"Level eg,College"}),
        'institution':forms.TextInput(attrs={'class':'sasa form-control',"PlaceHolder":"Institution"}),
        'dp':forms.FileInput(attrs={'class':'sasa form-control'}),
        'bio':forms.Textarea(attrs={'class':'sasa form-control',"PlaceHolder":"bios","rows":"4" }),
    }