from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import (
    CarListAPIView,
    CarDetailAPIView,
    MyObtainTokenPairView,
    RegisterView,
)

urlpatterns = [
    path('login/', include('rest_framework.urls')),
    path('api/', CarListAPIView.as_view()),
    path('api/<int:car_id>', CarDetailAPIView.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('api/register/', RegisterView.as_view(), name='auth_register'),
]