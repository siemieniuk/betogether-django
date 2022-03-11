from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .forms import LoginForm
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

class LoginView(View):
    template_name = 'login.html'
    def post(self, request):
        form = LoginForm(request.POST or None)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request,
                username=cd['username'],
                password=cd['password']
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(homepage)
                else:
                    return HttpResponse('You have been banned!')    
        form = LoginForm()
        return render(
            request,
            self.template_name,
            {
                'form': form,
                'msg': "Nieprawidłowe dane logowania"
            })

    def get(self, request):
        form = LoginForm()
        return render(
            request,
            self.template_name,
            {
                'form': form,
            })


def register(request):
    return render(
        request,
        'register.html'
    )
