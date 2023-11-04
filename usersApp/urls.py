from django.urls import path
from .views import *

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('account/', UserRetrieveAPIView.as_view(), name='account-detail'),
    path('delete-account/', UserDestroyAPIView.as_view(), name='delete-account'),
    path('update-account/', UserUpdateAPIView.as_view(), name='update-account'),
]
