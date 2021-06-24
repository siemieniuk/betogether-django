from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .forms import LoginForm
# Create your views here.


def index(request):
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
                    return HttpResponse('Success!')
                else:
                    return HttpResponse('You have been banned!')
            else:
                return HttpResponse('Invalid nickname or password')
        else:
            form = LoginForm()
            return render(
                request,
                self.template_name,
                {
                    'form': form,
                })

    def get(self, request):
        form = LoginForm()
        return render(
            request,
            self.template_name,
            {
                'form': form,
            })


def logout_view(request):
    logout(request)
    return render (
        request,
        'index.html',
        {
            'logout': True,
        }
    )


def register(request):
    return render(
        request,
        'register.html'
    )
