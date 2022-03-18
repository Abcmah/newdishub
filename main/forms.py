from dataclasses import field, fields
from email.headerregistry import Group
from django.forms import ModelForm
from .models import *
 
class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = '__all__'


class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields ='__all__'