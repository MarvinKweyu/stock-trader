from django.urls import path
from rest_framework.routers import SimpleRouter
from . import views


router = SimpleRouter()

router.register("users", views.UserViewSet, basename="users")

# registration endpoint
urlpatterns = router.urls
