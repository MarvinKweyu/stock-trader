from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets
from accounts.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    management of users
    """

    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
