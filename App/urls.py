from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings

# from django.conf.urls import include, url
from django.conf.urls.static import static

# from django.contrib import admin


urlpatterns = [
    path("", views.landingpage, name="landingpage"),
    path("<int:pk>_<str:website_name>/", views.websitepage, name="websitepage"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path(
        "<int:pk>_<str:website_name>/login/",
        views.login_view,
        name="login",
    ),
    path(
        "businesses/<int:pk>_<str:business_name>/",
        views.business_page,
        name="business-page",
    ),
    path(
        "<int:pk>_<str:website_name>/businesses/", views.businesses, name="businesses"
    ),
    path("<int:pk>_<str:website_name>/sales/", views.sales, name="sales"),
    path("<int:pk>_<str:website_name>/signup/", views.signup, name="signup"),
    path(
        "<int:pk>_<str:website_name>/new_business/",
        views.new_business,
        name="new_business",
    ),
    path("<int:pk>_<str:website_name>/new_sale/", views.new_sale, name="new_sale"),
    path("<int:pk>_<str:website_name>/premium/", views.premium, name="premium"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
