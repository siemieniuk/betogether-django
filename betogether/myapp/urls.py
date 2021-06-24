from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('terms_and_conditions', views.terms, name='terms_and_conditions'),
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.logout_view),
    path('register', views.register, name='register')
]
