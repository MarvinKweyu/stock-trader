from django.urls import path
from rest_framework.routers import SimpleRouter
from . import views


router = SimpleRouter()

router.register("products", views.ProductViewSet, basename="products")
router.register("reorders", views.ReorderViewset, basename="reorders")

# registration endpoint
urlpatterns = router.urls
