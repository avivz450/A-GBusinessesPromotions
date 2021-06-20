import pytest
from django.urls import reverse
from django.contrib.auth.models import User


@pytest.mark.django_db
class TestLogin:
    demo_webpage_login_url = reverse("login", args=[1, "Website_Demo"])
    demo_webpage_url = reverse("websitepage", args=[1, "Website_Demo"])

    @pytest.fixture
    def invalid_user_details(self):
        return {"username": "Aviv12", "password": "LiorLior"}

    def test_get_login_page(self, client):
        response = client.get(self.demo_webpage_login_url)
        assert response.status_code == 200

    def test_success_login_post_redirect(self, client, valid_user_details):
        response = client.post(self.demo_webpage_login_url, valid_user_details)
        assert response.status_code == 302  # redirect
        assert response.url == self.demo_webpage_url

    def test_login(self, client, valid_user_details):
        client.logout()
        response = client.get(self.demo_webpage_url)
        assert not response.wsgi_request.user.is_authenticated  # logged out
        client.post(self.demo_webpage_login_url, valid_user_details)
        response = client.get(self.demo_webpage_url)
        assert response.wsgi_request.user.is_authenticated  # successfully logged in

    def test_unsuccessful_login_post_not_redirect(self, client, invalid_user_details):
        response = client.post(self.demo_webpage_login_url, invalid_user_details)
        assert response.status_code == 200  # not redirected

    def test_unsuccessful_login_post_message(self, client, invalid_user_details):
        response = client.post(self.demo_webpage_login_url, invalid_user_details)
        assert "Invalid username/password." in str(response.content)

    def test_authenticated_user_view(self, client, valid_user_details):
        user = User.objects.get(username=valid_user_details["username"])
        client.force_login(user)
        response = client.get(self.demo_webpage_url)
        assert "Login" not in str(response.content)
        assert "Logout" in str(response.content)
