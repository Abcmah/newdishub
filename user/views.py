from email import message
from multiprocessing import context
from urllib import request
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import *
from .forms import *
# Create your views here.

def sign_up(request):
    form =  Sign_up_form()
    if request.method =="POST":
        form = Sign_up_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login-form')
    context={
        "form":form
    }
    return render(request,'user/register.html',context)

def login_user(request):
    user_entry = request.POST.get('username')
    user_pass = request.POST.get('password')
    user = authenticate(request,username=user_entry,password=user_pass)
    if user is not None:
        login(request,user)
        return redirect('home')
    return render(request,'user/login.html')

def logout_usr(request):
    logout(request)
    return redirect("login-form")
@login_required(login_url='login-form')
def profile_update(request,usr):
    usr = request.user
    form = Profile_form(instance=usr)
    if request.method =='POST':
        form = Profile_form(request.POST,request.FILES,instance=usr)
        form.save()
        messages.success(request,f'profile updated')
        return redirect('profile',usr)
    context = {
        'form':form
    }
    return render(request,'user/profile-form.html',context)
@login_required(login_url='login-form')
def creat_text_post(request):
    form = Text_post_form()
    if request.method == 'POST':
        form = Text_post_form(request.POST)
        f = form.save(commit=False)
        f.creater = request.user
        f.save()
        return redirect('view-text-post')
    else:
        form = Text_post_form()
    context={
        "form":form
    }
    return render(request,'main/text-post.html',context)

def text_post_view(request,pk):
    post = Text_post.objects.get(id=pk)
    comments = Comment.objects.filter(text_post=post)
    if request.method == 'POST':
        comment = request.POST.get('comment')
        Comment.objects.create(
            creater = request.user,
            text = comment,
            text_post =post,

        )
        return redirect('text-post-view',post.id)
    context ={
        'post':post,
        'comments':comments
    }
    return render(request,'main/text-view.html',context)

def delete_comment(request,pk):
    item = Comment.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('text-post-view',item.text_post.id)
    return render(request,'delete.html')


def delete_text_post(request,pk):
    item = Text_post.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        messages.error(request, f'Post deleted')
        return redirect('home')
    return render(request,'delete.html')

def create_photo_post(request):
    form = Photo_post_form()
    usr = request.user
    if request.method == 'POST':
        form = Photo_post_form(request.POST,request.FILES)
        new = form.save(commit=False)
        new.creater = usr
        new.save()
        print()
        messages.success(request, f'photo uploaded Successively  ')
        return redirect('home')
    else:
        form = Photo_post_form()
    context = {
        'forms':form
    }
    return render(request,'main/photo-post.html',context)

def delete_photo_post(request,pk):
    item = Photo_post.objects.get(id=pk)
    if request.method =='POST':
        item.delete()
        messages.error(request, f'post was delete')
        return redirect('home')
    return render(request,'delete.html')

def view_photo_post(request,pk):
    item = Photo_post.objects.get(id=pk)
    comments = Comment_photo_post.objects.filter(photo_post=item).order_by('created')
    no = comments.count()
    if request.method == "POST":
        text = request.POST.get('body-text')
        Comment_photo_post.objects.create(
            creater = request.user,
            photo_post = item,
            text = text
        )
        messages.success(request, f'you added a comment')
        return redirect('view_photo_post',item.id)
    context = {
        'item':item,
        'comments':comments,
        'no':no
    }
    return render(request,'main/photo-post-view.html',context)

def photo_comment_delete(request,pk):
    item = Comment_photo_post.objects.get(id=pk)
    print(item.id)
    photo = item.photo_post
    if request.method =='POST':
        item.delete()
        messages.error(request, f'deleted')
        return redirect('view_photo_post',photo.id)
    return render(request,'delete.html')
    

def profile(request,usr):
    user = User.objects.get(username=usr)
    context={
        'userp':user
    }
    return render(request,'user/profile.html',context)

def photo_like(request,pk):
    photo_post = Photo_post.objects.get(id=pk)
    if request.method =="POST":
        Likes.objects.create(
            liker = request.user,
            post = photo_post,
            liked = True
        )
        return redirect('home')
    return render(request,'main/home.html')
