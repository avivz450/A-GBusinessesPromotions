from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings

# from django.conf.urls import include, url
from django.conf.urls.static import static

# from django.contrib import admin


urlpatterns = [
    path("", views.landingpage, name="landingpage"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="home/login.html"),
        name="login",
    ),
    path(
        "businesses/<int:pk>_<str:business_name>/",
        views.business_page,
        name="business-page",
    ),
    path("businesses/", views.businesses, name="businesses"),
    path("sales/", views.sales, name="sales"),
    path("signup/", views.signup, name="signup"),
    path("new_business/", views.new_business, name="new_business"),
    path("new_sale/", views.new_sale, name="new_sale"),
    path("premium/", views.premium, name="premium"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
