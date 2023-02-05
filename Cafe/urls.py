from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name=''),
    path('login', views.login, name='login'),
    path('registration', views.registration, name='registration'),
    path('signup', views.signup, name='signup'),
    path('success_page', views.success_page, name='success_page'),
    path('buttonaction', views.buttonaction, name='buttonaction'),



]
Login_REDIRECT_URL = '/'