from rest_framework import routers
from apps.users.api.api import UsuarioViewSet

router = routers.DefaultRouter()

router.register('', UsuarioViewSet, basename="users")

urlpatterns = router.urls