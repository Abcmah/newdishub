from django.urls import path
from . import views
from user import views as usrviews

urlpatterns = [
    path('', views.home , name='home'),
    path('group/<str:pk>', views.group_view , name='group-view'),
    path('group/topic/<str:pk>', views.topicView , name='topicView'),
    path('create-group', views.groupCreate, name="create-group"),
    path('add-topic/<str:pk>', views.add_topic, name="add_topic"),
    path('message-deletion/<str:pk>', views.delete_message, name="delete_message"),
    path('group-deletion/<str:pk>', views.delete_group, name="delete_group"),
    path('group-update/<str:pk>', views.update_group, name="group_update"),
    path('post-text/',usrviews.creat_text_post, name='create-text-post'),
    path('photo-post/',usrviews.create_photo_post, name='creat_photo_post'),
    path('post-text/<str:pk>/',usrviews.text_post_view, name='text-post-view'),
    path('post-text/<str:pk>/delete-comment',usrviews.delete_comment, name='text-post-view-cmdelete'),
    path('photo_post/<str:pk>/',usrviews.view_photo_post, name='view_photo_post'),
    path('post-text/delete-comment/<str:pk>/',usrviews.photo_comment_delete, name='photo-post-delete'),
    path('photo_post/<str:pk>/delete',usrviews.delete_photo_post, name='delete_photo_post'),
    path('profile/update/<str:usr>/',usrviews.profile_update, name='profile_update'),
    path('profile/<str:usr>/', usrviews.profile, name='profile'),
    path('sign-up/',usrviews.sign_up, name='sign-up'),
    path('logout',usrviews.logout_usr, name='logout'),
    path('like/<str:pk>/',usrviews.photo_like, name='like'),
    path('text-post',views.home_text, name='view-text-post')
   

    
]
