from django.urls import path, reverse_lazy
from django.contrib.auth.views import LoginView, logout_then_login, PasswordResetView
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic.base import RedirectView
from django.contrib.auth import views as auth_views
from .views import *

app_name = 'users'

urlpatterns = [
    #path('', login_required(main), name='main'),
    path('home/', RedirectView.as_view(url=reverse_lazy('home')), name='home'),
    path('login/', 
        LoginView.as_view(template_name='auth/login.html'),
        name='login'
    ),
    path('logout/',
        logout_then_login,
        name='logout'
    ),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='auth/password_reset.html', email_template_name='auth/password_reset_email.html', subject_template_name='auth/password_reset_subject.txt', success_url=reverse_lazy('users:password_reset_done')), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='auth/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='auth/password_reset_confirm.html',success_url=reverse_lazy('users:password_reset_complete')), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='auth/password_change_done.html'), name='password_reset_complete'),
    path('change-password/', auth_views.PasswordChangeView.as_view(template_name='auth/change-password.html', success_url=reverse_lazy('users:password_reset_complete')), name='chage_password'),
]