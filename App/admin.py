from django.contrib import admin
from .models import Profile, Business, Sale, Notification, Contact

admin.site.register(Profile)
admin.site.register(Business)
admin.site.register(Sale)
admin.site.register(Notification)
admin.site.register(Contact)
