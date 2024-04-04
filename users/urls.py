from django.urls import path
from users import views
from user.views import *

urlpatterns = [
    path("profile-update/", views.ProfileUpdateAPIView.as_view()),
    path('product/<int:pk>/', views.ProductRetrieveAPIView.as_view()),
    path('products/', views.ProductListAPIView.as_view()),
    path('register/', SignupView.as_view()),
    path('login/', SignInView.as_view()),
    path('verify/', VerifyView.as_view()),
]