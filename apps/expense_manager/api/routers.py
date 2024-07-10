from rest_framework.routers import DefaultRouter

from apps.expense_manager.api.api import ExpenseViewSet

router = DefaultRouter()

router.register(r'expense', ExpenseViewSet, basename='expense')

urlpatterns = router.urls