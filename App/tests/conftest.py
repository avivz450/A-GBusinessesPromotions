import pytest
from App.models import Profile
from django.contrib.auth.models import User


@pytest.fixture
def profile():
    profile = Profile.create(username="test_user", password="testtest", email="test@test.com")
    return profile


@pytest.fixture
def authenticated_user(client, request):
    user = User.objects.get(username='Aviv')
    client.force_login(user)
    return user


@pytest.fixture
def valid_user_details():
    return {"username": "Aviv", "password": "AvivAviv"}


@pytest.fixture
def logged_client(client):
    user = Profile.objects.all().get(user_id=1).user
    client.force_login(user)
    return client
