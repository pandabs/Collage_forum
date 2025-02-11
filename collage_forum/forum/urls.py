from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('register/',views.register, name='register'),
    path('login/',views.user_login, name='login'),
    path('contactus/',views.contactus, name='contactus'),
    path('forum/',views.forum_view, name='forum'),
    path('forum/<int:forum_id>/', views.forum_detail, name='forum_detail'),
    path('forum/create/', views.create_forum, name='create_forum'),
    path('logout/', views.logout_view, name='logout'),
    path('forum/<int:forum_id>/edit/', views.edit_forum, name='edit_forum'),
    path('forum/<int:forum_id>/delete/', views.delete_forum, name='delete_forum'),
    path('forum/<int:forum_id>/comment/', views.add_comment, name='add_comment'),
] 
