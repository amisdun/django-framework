from django.urls import path
from . import views

urlpatterns = [
    path('logn/', views.login, name='users-login'),
    path('register/', views.register, name='users-register'),
]
