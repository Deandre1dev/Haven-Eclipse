from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

# Create your views here.
# This veiw lets the users login
def user_login(request):
    """Renders a login page for the user
    """
    return render(request, 'authentication/login.html')

#  This veiw is used to authenticate and check if the user already exists.
def authenticate_user(request):
    """Checks if the user exist in the database

        :return: If the user is authenticated show thier account information, else redirect them to the login page
    """
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is None:
        return HttpResponseRedirect(
            reverse('user_auth:login')
        )
    else:
        login(request, user)
        return HttpResponseRedirect(
            reverse('user_auth:show_user')
    )

def show_user(request):
    """Renders a html template with the users information
    """
    print(request.user.username)
    return render(request, 'authentication/user.html', {
        "username": request.user.username,
        "password": request.user.password
})

# This veiw is used to register a new user.
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("user_auth:login")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="authentication/register.html", context={"register_form":form})

# This veiw logs the user out.
def user_logout(request):
    """This function logs a user out
    """
    logout(request)
    messages.success(request, ("You were successfully logged"))
    return render(request, 'authentication/logout.html')