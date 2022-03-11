from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('terms_and_conditions', views.terms, name='terms_and_conditions'),
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register', views.register, name='register'),
]
