from django.urls import path
from rest_framework import routers

from .views import CarAdViewSet, MinYearView

router = routers.DefaultRouter()
router.register(r'cars', CarAdViewSet)

urlpatterns = router.urls
urlpatterns.append(path('min_year/', MinYearView.as_view()))
