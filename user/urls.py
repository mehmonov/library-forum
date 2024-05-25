from django.contrib import admin
from django.urls import path, include
from .views import user_login, user_logout, user_register, user_profile
urlpatterns = [
    path('', user_login.as_view(), name='user_login'),
    path('user_register', user_register.as_view(), name='user_register'),
    path('user_profile', user_profile, name='user_profile'),
    
    path('user_logout',user_logout, name='user_logout' )
]
