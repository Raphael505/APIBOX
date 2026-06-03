from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BoxViewSet

router = DefaultRouter()
router.register(r'boxes', BoxViewSet)   # 'boxes' é o nome que vai aparecer na URL

urlpatterns = [
    path('', include(router.urls)),     # Isso cria a API Root automaticamente
]