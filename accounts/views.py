from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render

from .forms import LoginForm, UserRegisterForm


def login_page(request):
   form = LoginForm(request.POST or None)

   if request.method == 'POST':
      if form.is_valid():
         email = form.cleaned_data.get('email')
         password = form.cleaned_data.get('password')

         user = authenticate(request, username=email, password=password)
         if user is not None:
            # login(request, user)
            print("LOGGED IN USER")
         else:
            print("USER IS NONE")
   context = {
      'form': form
   }
   return render(request, 'accounts/login.html', context)


def register_page(request):
   form = UserRegisterForm(request.POST or None)
   if request.method == 'POST':
      if form.is_valid():
         user = form.save(commit=False)
         user.first_name = 'first name here'
         user.last_name = 'last name here'
         user.other_name = 'other name here'
         user.save()
      else:
         print("no registered")

   context = {'form': form}
   return render(request, 'accounts/register.html', context)
