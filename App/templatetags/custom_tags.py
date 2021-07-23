from django import template
from App.models import Notification, Profile

register = template.Library()


@register.inclusion_tag("home/show_notifications.html", takes_context=True)
def show_notifications(context, website):
    request_user = context["request"].user
    logged_in_profile = Profile.objects.filter(user=request_user).first()
    notifications = (
        Notification.objects.filter(to_user=logged_in_profile)
        .exclude(user_has_seen=True)
        .order_by("-date")
    )
    return {"notifications": notifications, "website": website}
