
from django.urls import path, include
from django.contrib import admin
from accounts import urls
from rest_framework import permissions
from rest_framework.documentation import include_docs_urls

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


API_TITLE = "Stock Trader API"
API_DESCRIPTION = "Stock management and re-ordering"

schema_view = get_schema_view(
    openapi.Info(
        title="Stock Trader API",
        default_version="v1",
        description="Stock management and re-ordering",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("api-auth/", include("rest_framework.urls")),
    path("auth/", include("dj_rest_auth.urls")),  # api login
    path("accounts/", include("accounts.urls")),
    path("store/", include("localstore.urls")),
    path("docs/", schema_view.with_ui("redoc",
                                      cache_timeout=0), name="schema-redoc"),
]
