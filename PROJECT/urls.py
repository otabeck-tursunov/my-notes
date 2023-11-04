from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="My-Notes API",
        default_version='v1',
        description='"My Notes" is a web application that allows users to create, read, update, and delete their personal notes. '
                    'Users can register for an account, log in, and securely manage their notes. This application provides a simple '
                    'and user-friendly interface for organizing and accessing personal notes from anywhere with an internet connection.',
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="tursunovotabekkuva@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('usersApp.urls')),
    path('', include('notesApp.urls')),

    # simple-jwt
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # drf-yasg
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
