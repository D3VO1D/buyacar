from rest_framework import routers

from .views import CarAdViewSet

router = routers.DefaultRouter()
router.register(r'cars', CarAdViewSet)

urlpatterns = router.urls
