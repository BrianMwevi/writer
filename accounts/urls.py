from django.urls import path 
from django.urls import reverse_lazy
from .views import SignUpView
from django.contrib.auth import views as auth_views
from .forms import LoginForm

app_name = 'accounts'

urlpatterns = [
	path('register/', SignUpView.as_view(), name='register'),
	path('login/', auth_views.LoginView.as_view(template_name='accounts/register.html', success_url=reverse_lazy('writersapp:home')), name='login'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout', kwargs={'next_page':'writersapp:home'}),
]