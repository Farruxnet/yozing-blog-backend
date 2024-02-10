from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from bot.views import hook

schema_view = get_schema_view(
    openapi.Info(
        title="Yozing.Blog",
        default_version='v1',
        description="REST API for Yozing.Blog",
        terms_of_service="https://yozing.blog/terms/",
        contact=openapi.Contact(email="contact@yozing.blog"),
        license=openapi.License(name="Private"),
    ),
    public=True,
    permission_classes=[permissions.IsAdminUser,]
)


urlpatterns = [
    path('__admin/', admin.site.urls),
    path('bot-hook/', csrf_exempt(hook)),
    path('user/', include('users.urls')),

    path('api/docs/swagger<format>', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('api/docs/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger'),
]
