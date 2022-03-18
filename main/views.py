
from email import message
from multiprocessing import context
from os import name
from pydoc_data import topics
from urllib import request
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from user.models import *
from main import forms
# Create your views here.
def home(request):
    groups = Group.objects.all()
    text_posts = Text_post.objects.all().order_by('-created')
    photo_post = Photo_post.objects.all().order_by('-created')
    com = Comment_photo_post.objects.all()
    context={
        'groups':groups,
        'inc':0,
        'comments':com,
        'text_posts':text_posts,
        'photo_post':photo_post
    }
    return render(request,'main/home.html',context)

def home_text(request):
    text_posts = Text_post.objects.all().order_by('-created')
    context={
        'text_posts':text_posts,
    }
    return render(request,'main/home-text.html',context)


@login_required(login_url='login-form')
def groupCreate(request):
    form = GroupForm()
    group = Group.objects.all()
    if request.method =='POST':
        name = request.POST.get('namee')
        about = request.POST.get('about')
        f = form.save(commit=False)
        f.name = name
        f.description = about
        f.host = request.user
        f.save()
        f.participants.add(request.user)
        messages.success(request, f'Successively added >> ')
        return redirect("home")
    context = {
        "form":form
    }

    return render(request,'main/groupform.html',context)


def group_view(request,pk):
    group = Group.objects.get(id=pk)
    topics =Topic.objects.filter(group=group).order_by("-created")
    participants = group.participants.all()
    no_of_participants = participants.count()
    print(no_of_participants)
    context={
        "group":group,
        "no_p":no_of_participants,
        "topics":topics
    }
    return render(request,'main/groupView.html',context)

def add_topic(request,pk):
    g = Group.objects.get(id=pk)
    topics =Topic.objects.filter(group=g)
    form = TopicForm()
    count = topics.count()
    
    print(f'topics {count}')
    
    user_topic = request.POST.get('topic')
    if request.method =='POST':
        f = form.save(commit=False)
        f.topic = user_topic
        f.creater = request.user
        f.discription = request.POST.get('about')
        f.group = g
        f.save()
        if not f.creater in  g.participants.all():
            g.participants.add(f.creater)
        return redirect('group-view',g.id)
    context ={
        "form":form,
    }
    return render(request,'main/topic.html',context)   


def topicView(request,pk):
    topics = Topic.objects.get(id=pk)
    messages = Message.objects.filter(topic=topics)
    print(f"hi there you {topics}")
    if request.method == "POST":
        Message.objects.create(
            host = request.user,
            topic = topics,
            body = request.POST.get('body-text')
        )
        
        
        return redirect("topicView",topics.id)
    context={
        "topics":topics,
        "messages":messages
    }

    return render(request,'main/topicView.html',context)

def delete_message(request,pk):
    message = Message.objects.get(id=pk)
    if request.method =='POST':
        message.delete()
        message.error(request,f'message delete')
        return redirect("topicView",message.topic.id)
    context={
        "object":message
    }
    return render(request,'delete.html',context)


def delete_group(request,pk):
    group = Group.objects.get(id=pk)
    if request.method =='POST':
        group.delete()
        return redirect('home')
    context={
        'group':group,
        'object':group
    }
    return render(request,'delete.html',context)

def update_group(request,pk):
    group = Group.objects.get(id=pk)
    form = GroupForm(instance=group)
    if request.method == "POST":
        form = GroupForm(request.POST,instance=group)
        f = form.save(commit=False)
        f.save()
        return redirect('group-view',f.id)
    context ={
        
    }
    return render(request,'main/groupform.html')