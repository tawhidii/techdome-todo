from django.urls import path
from .views import (
    CustomTokenObtainPairView,
    RegistrationView
)

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
