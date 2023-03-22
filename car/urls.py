from django.urls import include, path
from . import views
from .views import (
    CarListAPIView,
    CarDetailAPIView,
)

urlpatterns = [
    path('api/', CarListAPIView.as_view()),
    path('api/<int:car_id>', CarDetailAPIView.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('api/auth/', views.LoginView.as_view()),
]