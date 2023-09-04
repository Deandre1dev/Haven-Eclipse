from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.

# NewUserForm used to create a form where the user can register.
class NewUserForm(UserCreationForm):
	"""NewUserForm creates a for for a new user to register

	:param first_name: A field to include the users first name in the form
	:param fields: A list of fields that are included in the form in the order specified
	"""
	
	first_name = forms.CharField(max_length=5000)

	class Meta:
		model = User
		fields = ("username", "first_name", "password1", "password2")

	def save(self, commit=True):
		"""The save function checks if the form is successfully filled in and saves it as a new user in the database
		"""

		user = super(NewUserForm, self).save(commit=False)
		user.first_name = self.cleaned_data['first_name']
		if commit:
			user.save()
		return user