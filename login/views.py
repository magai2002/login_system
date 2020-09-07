from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse

def index(request):
	return render(request, 'index.html', {})

def loginPage(request):
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, "Username or Password is incorrect. Try Again...")

	return render(request, 'login.html', {})

def register(request):
	form = RegisterForm()

	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request, 'Account was created for ' + user + '!')
			return redirect('login')
		else:
			messages.info(request, 'Passwords did not match, try again')

	context = {'form': form}
	return render(request, 'register.html', context)


def homePage(request):
	return render(request, 'home.html', {})