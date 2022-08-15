from django.contrib import admin
from django.urls import path
from l_app import views

# template tagging

app_name = 'l_app'

urlpatterns = [
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other'),
    path('user_login/', views.user_login, name='user_login'),
    path('register/', views.register, name='register'),

]
