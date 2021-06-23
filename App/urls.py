from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings

# from django.conf.urls import include, url
from django.conf.urls.static import static

# from django.contrib import admin


urlpatterns = [
    path("", views.landingpage, name="landingpage"),
    path(
        "websites/<int:pk>_<str:website_name>/", views.websitepage, name="websitepage"
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path(
        "websites/<int:pk>_<str:website_name>/login/",
        views.login_view,
        name="login",
    ),
    path(
        "websites/<int:website_pk>_<str:website_name>/edit_profile/<int:profile_pk>/",
        views.edit_profile,
        name="edit_profile",
    ),
    path(
        "websites/<int:webpage_pk>_<str:website_name>/businesses/<int:business_pk>_<str:business_name>/",
        views.business_page,
        name="business-page",
    ),
    path(
        "websites/<int:website_pk>_<str:website_name>/edit_business/<int:business_pk>/",
        views.edit_business,
        name="edit_business",
    ),
    path(
        "websites/<int:pk>_<str:website_name>/edit_business/",
        views.choose_business_to_edit,
        name="choose_business_to_edit",
    ),
    path(
        "websites/<int:pk>_<str:website_name>/businesses/",
        views.businesses,
        name="businesses",
    ),
    path("websites/<int:pk>_<str:website_name>/sales/", views.sales, name="sales"),
    path("websites/<int:pk>_<str:website_name>/signup/", views.signup, name="signup"),
    path(
        "websites/<int:pk>_<str:website_name>/new_business/",
        views.new_business,
        name="new_business",
    ),
    path(
        "websites/<int:pk>_<str:website_name>/new_sale/",
        views.new_sale,
        name="new_sale",
    ),
    path(
        "websites/<int:website_pk>_<str:website_name>/edit_sale/<int:sale_pk>/",
        views.edit_sale,
        name="edit_sale",
    ),
    path(
        "websites/<int:pk>_<str:website_name>/edit_sale/",
        views.choose_sale_to_edit,
        name="choose_sale_to_edit",
    ),
    path(
        "websites/<int:pk>_<str:website_name>/premium/", views.premium, name="premium"
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
