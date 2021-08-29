import pytest
from django.urls import reverse
from django.contrib.auth.models import User


@pytest.mark.django_db
class TestLogin:
    demo_webpage_login_url = reverse("login", args=[1, "Website Demo"])
    demo_webpage_url = reverse("websitepage", args=[1, "Website Demo"])

    @pytest.fixture
    def invalid_user_details(self):
        return {"username": "Aviv12", "password": "Aviv12Aviv12"}

    def test_get_login_page(self, client):
        response = client.get(self.demo_webpage_login_url)
        assert response.status_code == 200

    def test_unsuccessful_login_post_not_redirect(self, client, invalid_user_details):
        response = client.post(self.demo_webpage_login_url, invalid_user_details)
        assert response.status_code == 200  # not redirected

    def test_authenticated_user_view(self, client, valid_user_details):
        user = User.objects.get(username=valid_user_details["username"])
        client.force_login(user)
        response = client.get(self.demo_webpage_url)
        assert "Login" not in str(response.content)
        assert "Logout" in str(response.content)
