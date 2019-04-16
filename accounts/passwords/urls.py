# accounts.passwords.urls.py 
from django.urls import path, re_path
from django.contrib.auth import views as auth_views

urlpatterns  = [
path('password/change/', 
        auth_views.PasswordChangeView.as_view(template_name='accounts/pass_reset.html'), 
        name='password_change'),
path('password/change/done/',
        auth_views.PasswordChangeDoneView.as_view(), 
        name='password_change_done'),
path('password/reset/', 
        auth_views.PasswordResetView.as_view(), 
        name='password_reset'),
path('password/reset/done/', 
        auth_views.PasswordResetDoneView.as_view(), 
        name='password_reset_done'),
re_path('password/reset/\
        (?P<uidb64>[0-9A-Za-z_\-]+)/\
        (?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', 
        auth_views.PasswordResetConfirmView.as_view(template_name='writersapp:home'), 
        name='password_reset_confirm'),

path('password/reset/complete/', 
        auth_views.PasswordResetCompleteView.as_view(), 
        name='password_reset_complete'),
]