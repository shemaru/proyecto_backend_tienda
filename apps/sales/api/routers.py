from rest_framework.routers import DefaultRouter
from apps.sales.api.api import SalesViewSet

router = DefaultRouter()

router.register(r'sales',SalesViewSet, basename='sales')

urlpatterns =  router.urls