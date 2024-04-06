from django.urls import path
from .views.product_views import get_all, get_my_products, create_product, update_product, delete_product
from .views.order_views import get_my_orders, create_order, update_order, delete_order
from .views.auth_views import MyTokenObtainPairView, UserRegistrationView
from rest_framework_simplejwt.views import ( TokenRefreshView)

urlpatterns = [
    path('token/',  MyTokenObtainPairView.as_view()),
    path('token/refresh/',  TokenRefreshView.as_view(), name='token_refresh'),
    path('register/',   UserRegistrationView.as_view()),
    
    path('products/', get_all, name="get_products"),
    path('products/get_my_products/', get_my_products, name="get_my_products"),
    path('products/create/', create_product, name="create_product"),
    path('products/<int:pk>/update/', update_product, name="update_product"),
    path('products/<int:pk>/delete/', delete_product, name="delete_product"),
    
    path('orders/get_my_orders/', get_my_orders, name="get_my_orders"),
    path('orders/create/', create_order, name="create_order"),
    path('orders/<int:pk>/update/', update_order, name="update_order"),
    path('orders/<int:pk>/delete/', delete_order, name="delete_order"),
]