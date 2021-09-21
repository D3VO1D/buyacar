from django.urls import path
from rest_framework import routers

from .views import CarAdViewSet, MinYearView, CarMakesView, UserCityView

router = routers.DefaultRouter()
router.register(r'cars', CarAdViewSet)

urlpatterns = router.urls
urlpatterns += [
    path('min_year/', MinYearView.as_view()),
    path('usercity/', UserCityView.as_view()),
    path('makes/', CarMakesView.as_view())
]
