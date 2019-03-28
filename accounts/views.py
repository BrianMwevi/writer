from django.shortcuts import render
from django.views.generic import CreateView
from .forms import SignupForm, LoginForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth import get_user_model, authenticate, login, logout


from django.urls import reverse_lazy
# Create your views here.
class SignUpView(CreateView):
	# fields = ('username', 'email', 'password1', 'password2')
	form_class = SignupForm
	model = get_user_model()
	success_url = reverse_lazy('accounts:signup')
	template_name = 'accounts/register.html'

def register(request):
	if request.user.is_active:
		return HttpResponseRedirect(reverse_lazy("home"))
	login_form = LoginForm()
	signup_form = SignupForm()
	is_user = True
	if request.method == "POST":
		if request.POST.get("email"):
			form = SignupForm(data=request.POST)
			if form.is_valid():
				user = form.save()	
				return HttpResponseRedirect(reverse_lazy("accounts:register"))
			else:
				signup_form = form
				is_user = False
		else:
			form = LoginForm(data=request.POST)
			if form.is_valid():
				username = request.POST.get("username")
				password = request.POST.get("password")
				user = authenticate(username=username, password=password)

				if user is not None:
					# if user.is_active:
					login(request, user)
					return HttpResponseRedirect(reverse_lazy("home"))
				else:
					print(user)
			if form.errors:
				login_form = form
	return render(request, 'accounts/register.html', {"login_form":login_form, "signup_form":signup_form, "is_user":is_user})
