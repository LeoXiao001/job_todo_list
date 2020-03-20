from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    # path('login/', views.user_login, name='login'),
    path('', views.dashboard, name='dashboard'),
    path('create_list/', views.todolist_create, name='list_create'),
    path('create_item/<int:list_id>', views.todoitem_create, name='item_create'),
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
