from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('base/', views.base, name='base'),
    path('', views.landingpage, name='landingpage'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
