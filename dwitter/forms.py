from django import forms
from .models import Dweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DweetForm(forms.ModelForm):
    body = forms.CharField(
	required=True,
	widget=forms.widgets.Textarea(
		attrs={
			"placeholder": "Wat heb je te zeuren?",
			"class": "textarea is-succes is-medium",
			}
		),
		label="",
	)

    class Meta:
        model = Dweet
        exclude = ("user", )

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user
