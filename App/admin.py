from django.contrib import admin
from .models import (
    Profile,
    Business,
    Sale,
    Notification,
    Contact,
    Website,
    Website_Profile,
)

admin.site.register(Profile)
admin.site.register(Business)
admin.site.register(Sale)
admin.site.register(Notification)
admin.site.register(Contact)
admin.site.register(Website)
admin.site.register(Website_Profile)
