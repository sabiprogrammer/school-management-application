from django.shortcuts import render, redirect
from django.http import HttpResponse


def check_not_authenticated(a_function):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return a_function(request, *args, **kwargs)

    return wrapper_function


def allowed_users(allowed_roles=[]):
    def decorators(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("You are not allowed to view this page")

        return wrapper_func
    return decorators


def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'customers':
            return redirect('user')

        if group == 'admin':
            return view_func(request, *args, **kwargs)
    return wrapper_function

