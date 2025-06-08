from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'provinces', views.ProvinceViewSet, basename='provinces')
router.register(r'channels', views.ChannelViewSet, basename='channels')
router.register(r'posts', views.PostViewSet, basename='posts')
router.register(r'category', views.CategoryViewSet, basename='category')
router.register(r'platform-token', views.PlatformTokenViewSet, basename='platform-token')

urlpatterns = [
    path('', include(router.urls)),
]