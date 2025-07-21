from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet, CustomerViewSet

router = DefaultRouter()
router.register('orders', OrderViewSet)
router.register('customers', CustomerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
