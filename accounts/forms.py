from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

class SignupForm(UserCreationForm):
	
	class Meta:
		model = get_user_model()
		fields = ('username', 'email', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		field_class = "form-control,btn-custom, form_create"
		self.fields['username'].widget.attrs.update({"placeholder": "Username","id":"id_loginusername", "class": field_class})
		self.fields['email'].widget.attrs.update({"required":True,"placeholder": "example@gmail.com","class": field_class})
		self.fields['password1'].widget.attrs.update({"placeholder": "Password","class": field_class})
		self.fields['password2'].widget.attrs.update({"placeholder": "Confirm password","class": field_class})
		for fieldname in ['username', 'password1', 'password2']:
			self.fields[fieldname].help_text = None

class LoginForm(AuthenticationForm):

	class Meta:
		model = get_user_model()
		fields = ('username', 'password',)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		field_class = "form-control,btn-custom, form_create"
		self.fields['username'].widget.attrs.update({"placeholder": "Username","class": field_class})
		self.fields['password'].widget.attrs.update({"placeholder": "Password","class": field_class})
