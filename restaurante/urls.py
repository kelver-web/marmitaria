from django.contrib import admin
from django.urls import path
from restaurante import views
from django.views.generic import RedirectView


urlpatterns = [
    path('index/', views.index),
    path('index/submit', views.pedido),
    path('ver_pedido/', views.ver_pedido),
    path('deletar/<int:id>/', views.deletar, name='deletar'),
    path('', RedirectView.as_view(url='/index/')),
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user),
    path('register/', views.register),
    path('register/submit', views.register),
]