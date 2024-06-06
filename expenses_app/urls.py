from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExpenseViewSet, register

router = DefaultRouter()
router.register(r'expenses', ExpenseViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', register, name='register'),
]
