from django.urls import include, path
from . import views
from .views import (
    CarListAPIView,
    CarDetailAPIView,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('api/', CarListAPIView.as_view()),
    path('api/<int:car_id>', CarDetailAPIView.as_view()),
    path('login/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]