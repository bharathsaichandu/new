from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView
from forum.views import (
    signup,home,ask_question,question_list_view,question_detail_view,question_edit_view,
    question_delete_view,profile,sharedroompost,privateroompost,entirehousepost,change_password,searchview,sharedroom_list_view,house_detail_view
,sharedroompostedit,privateroom_list_view,privateroom_detail_view,entirehouse_detail_view
,entirehouse_list_view,entirehousepostedit,privateroompostedit)

from django.contrib.auth import views as auth_views
urlpatterns = [
    path('search/',searchview,name='search'),
    path('signup/', signup, name='signup'),
    path('login/', auth_views.login, {'template_name': 'login.html'}, name='login'),
    path('logout/', auth_views.logout, {'next_page': 'login'}, name='logout'),
    path('password_change/',change_password,name='change_password'),
    path('profile/', profile, name='profile'),
    path('ask_question/',ask_question,name='ask_question'),
    path('post_private_room',privateroompost,name='privateroompost'),
    path('post_share_room/',sharedroompost,name='sharedroompost'),
    path('post_entire_house/',entirehousepost,name='entirehousepost'),
    path('question_list/<int:my_id>/edit/',question_edit_view,name='edit_question'),
    path('question_list/',question_list_view,name='question_list'),
    path('house_list/',sharedroom_list_view, name='house_list'),
    path('privateroomlist/',privateroom_list_view,name='privateroomlist'),
    path('entirehouselist/', entirehouse_list_view, name='entirehouselist'),
    path('house_list/<int:my_id>/',house_detail_view,name='house-detail'),
    path('privateroomlist/<int:my_id>/',privateroom_detail_view,name='privateroom-detail'),
path('privateroomlist/<int:my_id>/edit',privateroompostedit,name='privateroomedit'),
    path('entirehouselist/<int:my_id>/',entirehouse_detail_view,name='entirehouse-detail'),
path('entirehouselist/<int:my_id>/edit',entirehousepostedit,name='entirehouseedit'),
    path('house_list/<int:my_id>/edit', sharedroompostedit, name='shared_room_edit'),
    path('question_list/<int:my_id>/',question_detail_view,name='question-detail'),
    path('question_list/<int:my_id>/delete/',question_delete_view,name='question-delete'),
    path('',home,name='home'),
    path('password-reset/', auth_views.password_reset,
         {'template_name': 'password_reset.html'},
         name='password_reset'),

    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='password_reset_complete.html'
         ),
         name='password_reset_complete'),
]
