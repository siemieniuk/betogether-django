'''Here are implemented URLs for app "myapp"'''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('terms_and_conditions', views.terms, name='terms_and_conditions'),
    path('register', views.register, name='register'),
    path('settings', views.settings, name='account_settings'),
]
