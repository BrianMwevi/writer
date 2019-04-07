from django.urls import path 
from django.urls import reverse_lazy
from .views import register
from django.contrib.auth import views as auth_views
from .forms import LoginForm

app_name = 'accounts'

urlpatterns = [
	path('register/', register, name='register'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout', kwargs={'next_page':'writersapp:home'}),
]