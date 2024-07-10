from rest_framework.routers import DefaultRouter
from apps.products.api.viewsets.viewset_product import ProductViewSet
from apps.products.api.viewsets.viewsets_general import *

router = DefaultRouter()

router.register(r'products',ProductViewSet, basename='products')
router.register(r'unit_of_measurement',UnitOfMeasurementViewSet, basename='unit_of_measurement')
router.register(r'category',CategoryViewSet, basename= 'category')
router.register(r'discount',DiscountViewSet, basename='discount')

urlpatterns =  router.urls