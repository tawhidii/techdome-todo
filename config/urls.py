from rest_framework import permissions
from django.contrib import admin
from django.urls import path, include,re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Todos API",
      default_version='v1',
      description="An api doc for todos API project given by Techdome Solutions Private Limited",
      contact=openapi.Contact(email="contact@todosapi.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,)
)


urlpatterns = [

    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.api.urls')),
    path('todos/',include('todos.api.urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
