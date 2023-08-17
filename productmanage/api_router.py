from rest_framework.routers import SimpleRouter, DefaultRouter

from users.api import UserViewSet
from product.api import ProductViewSet

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('product', ProductViewSet)

app_name = 'api'
urlpatterns = router.urls