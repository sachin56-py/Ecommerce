from django.urls import path
from authentications import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register')
    
]