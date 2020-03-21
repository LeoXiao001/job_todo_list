from django.urls import path
from django.contrib.auth import views as auth_views
from .views import TodoitemDetailView, TodolistDetailView
from . import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    # list related
    path('create_list/', views.todolist_create, name='list_create'),
    path('list_detail/<int:pk>', TodolistDetailView.as_view(), name='list_detail'),
    # item related
    path('create_item/<int:list_id>', views.todoitem_create, name='item_create'),
    path('item_detail/<int:pk>', TodoitemDetailView.as_view(), name='item_detail'),
    # user login/out
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # chagne password urls
    path('password_change/',
        auth_views.PasswordChangeView.as_view(),
        name='password_change'),
    path('password_change/done/',
        auth_views.PasswordChangeDoneView.as_view(),
        name='password_change_done'),
    # reset password urls
    path('password_reset/',
        auth_views.PasswordResetView.as_view(),
        name='password_reset'),
    path('password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'),
    path('reset/don/',
        auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete'),
    path('register/', views.register, name='register'),
]
