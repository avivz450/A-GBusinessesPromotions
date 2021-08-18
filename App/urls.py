from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from .views import RemoveNotification

# from django.conf.urls import include, url
from django.conf.urls.static import static


urlpatterns = (
    [
        path("", views.landingpage, name="landingpage"),
        path("websites/", views.choose_website, name="choose_website"),
        path(
            "login/",
            auth_views.LoginView.as_view(template_name="home/landingpage_login.html"),
            name="landingpage_login",
        ),
        path("signup/", views.landingpage_signup, name="landingpage_signup"),
        path("add_website/", views.add_website, name="add_website"),
        path(
            """add_website/add_categories/<int:new_website_id>/<int:number_of_categories_to_submit>/
            <int:number_of_slides_to_submit>/""",
            views.add_categories,
            name="add_categories",
        ),
        path(
            "add_website/add_slides/<int:new_website_id>/<int:number_of_slides_to_submit>/",
            views.add_slides,
            name="add_slides",
        ),
        path(
            "websites/<int:pk>_<str:website_name>/",
            views.websitepage,
            name="websitepage",
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
            """websites/<int:webpage_pk>_<str:website_name>/businesses
            /<int:business_pk>_<str:business_name>/<int:additional_pictures>/""",
            views.business_additional_pictures,
            name="business_additional_pictures",
        ),
        path(
            "websites/<int:website_pk>_<str:website_name>/edit_business/<int:business_pk>/",
            views.edit_business,
            name="edit_business",
        ),
        path(
            "websites/<int:pk>_<str:website_name>/businesses/",
            views.businesses,
            name="businesses",
        ),
        path("websites/<int:pk>_<str:website_name>/sales/", views.sales, name="sales"),
        path(
            "websites/<int:pk>_<str:website_name>/signup/", views.signup, name="signup"
        ),
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
            "websites/<int:pk>_<str:website_name>/premium/",
            views.premium,
            name="premium",
        ),
        path(
            "notification/delete/<int:notification_pk>",
            RemoveNotification.as_view(),
            name="notification-delete",
        ),
        path(
            "websites/<int:pk>_<str:website_name>/admin-section/Businesses/",
            views.admin_businesses,
            name="admin_businesses",
        ),
        path(
            """websites/<int:pk>_<str:website_name>/admin-section/Businesses/
            <int:business_id>/<str:business_new_status>/""",
            views.change_business_status,
            name="change_business_status",
        ),
        path(
            "websites/<int:pk>_<str:website_name>/admin-section/Sales/<str:activated_filter>/",
            views.admin_sales,
            name="admin_sales",
        ),
        path(
            """websites/<int:pk>_<str:website_name>/admin-section/Sales/
        <int:sale_id>/<str:sale_new_status>/<str:activated_filter>/""",
            views.change_sale_status,
            name="change_sale_status",
        ),
        path(
            "websites/<int:pk>_<str:website_name>/connect_businesses/",
            views.connect_businesses_page,
            name="connect_businesses_page",
        ),
        path(
            "websites/<int:pk>_<str:website_name>/connect_businesses/<int:business_pk>/",
            views.connect_business,
            name="connect_business",
        ),
        path(
            "websites/<int:pk>_<str:website_name>/my_businesses/",
            views.my_businesses,
            name="my_businesses",
        ),
        path(
            "websites/<int:pk>_<str:website_name>/contact_us/",
            views.contact_us,
            name="contact_us",
        ),
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
