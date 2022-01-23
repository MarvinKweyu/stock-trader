import pytest
from accounts.models import CustomUser
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_user_create():
    """A user is created"""
    CustomUser.objects.create_user(
        username="testuser", email="testuser@mail.com", role="W", password="test")
    assert CustomUser.objects.count() == 1
    assert CustomUser.objects.get(username="testuser").role == "W"
