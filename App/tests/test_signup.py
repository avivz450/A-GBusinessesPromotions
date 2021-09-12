import pytest
from django.contrib.auth.models import User
from App.models import Profile
from pytest_django.asserts import assertTemplateUsed
from App.forms import SignUpForm
from django.urls import reverse


@pytest.mark.django_db
class TestSignUp:
    demo_webpage_url = reverse("websitepage", args=[1, "Tel Aviv"])
    demo_webpage_signup_url = reverse("signup", args=[1, "Tel Aviv"])

    @pytest.fixture
    def valid_signup_details(self):
        return {
            "username": "username",
            "email": "user@e.com",
            "password1": "ido123123",
            "password2": "ido123123",
        }

    def get_signup_page_status_code(self, client):
        response = client.get(self.demo_webpage_signup_url)
        assert response.status_code == 200

    def test_valid_signup(self, valid_signup_details, client):
        client.post(self.demo_webpage_signup_url, data=valid_signup_details)
        user = User.objects.filter(username=valid_signup_details["username"])
        assert user is not None
        profile = Profile.objects.filter(user=user)
        assert profile is not None

    @pytest.mark.parametrize(
        "invalid_signup_details",
        [
            # username cannot be empty
            [
                {
                    "username": "",
                    "email": "valid@email.com",
                    "password1": "pw123123",
                    "password2": "pw123123",
                },
                "username",
            ],
            # email invalid
            [
                {
                    "username": "valid_username",
                    "email": "a",
                    "password1": "pw123123",
                    "password2": "pw123123",
                },
                "email",
            ],
            # password to short
            [
                {
                    "username": "valid_username",
                    "email": "valid@email.com",
                    "password1": "123",
                    "password2": "123",
                },
                "password2",
            ],
            # passwords do not match
            [
                {
                    "username": "valid_username2",
                    "email": "valid@email.com",
                    "password1": "000000000",
                    "password2": "123456789",
                },
                "password2",
            ],
        ],
    )
    def test_invalid_signup(self, invalid_signup_details, client):
        response = client.post(
            self.demo_webpage_signup_url, data=invalid_signup_details[0]
        )
        user = User.objects.filter(
            username=invalid_signup_details[0]["username"]
        ).first()
        assert invalid_signup_details[1] in response.context["form"].errors
        assert user is None
        assert response.status_code == 200

    def test_valid_signup_redirection(self, valid_signup_details, client):
        response = client.post(self.demo_webpage_signup_url, data=valid_signup_details)
        assert response.status_code == 302
        assert response.url == self.demo_webpage_url

    def test_authenticated_user_view_signup(self, client, authenticated_user):
        response = client.get(self.demo_webpage_url)
        assert "Sign up" not in str(response.content)

    def test_unauthenticated_user_view_signup(self, client):
        response = client.get(self.demo_webpage_signup_url)
        assert "Sign up" in str(response.content)

    def test_signup_form_and_template_displayed(self, client):
        response = client.get(self.demo_webpage_signup_url)
        assert isinstance(response.context["form"], SignUpForm)
        assertTemplateUsed(response, "home/signup.html")
