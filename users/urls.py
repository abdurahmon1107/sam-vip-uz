from django.urls import path
from users import views


urlpatterns = [
    path("profile-update/", views.ProfileUpdateAPIView.as_view()),
    path('product/<int:pk>/', views.ProductRetrieveAPIView.as_view()),
]