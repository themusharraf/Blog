from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from root.settings import MEDIA_ROOT, MEDIA_URL
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Blog API",
        default_version='v1',
        description="Blog Api",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="All nc License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('blog.urls')),
                  path('auth/', include('auth.urls')),
                  re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

              ] + static(MEDIA_URL, document_root=MEDIA_ROOT)

# TODO: PERMISON CLLAS QILSI JERAK
