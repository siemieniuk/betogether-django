from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .forms import RegisterForm
# Create your views here.

def homepage(request):
    if request.user.is_authenticated:
        return render(
            request,
            'dashboard.html'
        )
    return render(
        request,
        'index.html'
    )

def terms(request):
    return render(
        request,
        'terms_and_conditions.html'
    )

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            cd = form.cleaned_data
            username=cd['username'],
            password=cd['password']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('homepage')
        return render(
            request,
            'register.html',
            {
                'form': form,
                'errors': form.errors
            }
        )
    else:
        form = RegisterForm()
    return render(
        request,
        'register.html',
        {
            'form': form
        }
    )

@login_required
def settings(request):
    return render(
        request,
        'settings.html'
    )
