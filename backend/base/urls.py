from django.urls import path
from .views.product_views import get_all, create_product, update_product, delete_product
from .views.auth_views import MyTokenObtainPairView, UserRegistrationView
from rest_framework_simplejwt.views import ( TokenRefreshView)

urlpatterns = [
    path('token/',  MyTokenObtainPairView.as_view()),
    path('token/refresh/',  TokenRefreshView.as_view(), name='token_refresh'),
    path('register/',   UserRegistrationView.as_view()),
    
    path('products/', get_all, name="get_products"),
    path('products/create/', create_product, name="create_product"),
    path('products/<int:pk>/update/', update_product, name="update_product"),
    path('products/<int:pk>/delete/', delete_product, name="delete_product")
]