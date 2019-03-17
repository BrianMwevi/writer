from django.shortcuts import render
from django.views.generic import CreateView
from .forms import SignupForm, LoginForm
from django.contrib.auth import get_user_model
User = get_user_model()

from django.urls import reverse_lazy
# Create your views here.
class SignUpView(CreateView):
	form_class = SignupForm
	model = User
	success_url = reverse_lazy('accounts:signup')
	template_name = 'accounts/signup.html'
	def get_context_data(self, **kwargs):
	    context = super().get_context_data(**kwargs)
	    context['login_form'] =  LoginForm
	    # context['action_url'] =  LoginForm
	    return context