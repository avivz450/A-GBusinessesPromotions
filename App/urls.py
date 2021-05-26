from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
# from django.conf.urls import include, url
from django.conf.urls.static import static
# from django.contrib import admin


urlpatterns = [
    path('base/', views.base, name='base'),
    path('', views.landingpage, name='landingpage'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='home/login.html'), name='login'),
    path('businesses/', views.businesses, name='businesses'),
    path('sales/', views.sales, name='sales'),
    path('signup/', views.signup, name='signup'),
] + static(settings.IMAGES_URL, document_root=settings.IMAGES_ROOT)
    