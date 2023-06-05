from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog.views import PostModeViewSet

router = DefaultRouter()
router.register(r'api', PostModeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/auth/', include('rest_framework.urls')),
    path('api/auth/', include('dj_rest_auth.urls')),
]
