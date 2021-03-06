from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView
from .forms import SignupForm, LoginForm, ResetPasswordForm
from writersapp.models import Post
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth import get_user_model, authenticate, login, logout, update_session_auth_hash
from django.contrib import messages


from django.urls import reverse_lazy
# Create your views here.

def register(request):
	if request.user.is_active:
		return HttpResponseRedirect("home")
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

def password_change(request):
	if request.method == 'POST':
		form = ResetPasswordForm(request.user, request.POST)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request,user)
			messages.success(request, 'Your password was successfully updated!')
			return redirect('home')
		else:
			messages.error(request, 'Please correct the error below.')
	else:
		form = ResetPasswordForm(request.user)
	return render(request, 'accounts/pass_reset.html', {
	'form': form
		})

class UserProfile(LoginRequiredMixin, ListView):
	model = get_user_model()
	login_url = "accounts:register"
	success_url = "home"
	template_name = "accounts/profile.html"

	def get_context_data(self, **kwargs):
	    context = super().get_context_data(**kwargs)
	    context["user_posts"] = Post.objects.filter(author=self.request.user)
	    context["drafts"] = Post.objects.filter(author=self.request.user, draft=True)
	    context["pub"] = Post.objects.filter(author=self.request.user, draft=False)
	    return context

