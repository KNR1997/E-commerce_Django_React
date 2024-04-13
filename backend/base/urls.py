from django.urls import path
from .views.product_views import get_products
from .views.order_views import get_my_orders, create_order, update_order, delete_order
from .views.auth_views import MyTokenObtainPairView, UserRegistrationView
from rest_framework_simplejwt.views import ( TokenRefreshView)
from .views.type_views import get_types

urlpatterns = [
    path('token/',  MyTokenObtainPairView.as_view()),
    path('token/refresh/',  TokenRefreshView.as_view(), name='token_refresh'),
    path('register/',   UserRegistrationView.as_view()),
    
    path('products', get_products, name="get_products"),

    path('orders/get_my_orders/', get_my_orders, name="get_my_orders"),
    path('orders/create/', create_order, name="create_order"),
    path('orders/<int:pk>/update/', update_order, name="update_order"),
    path('orders/<int:pk>/delete/', delete_order, name="delete_order"),
    
    path('types/', get_types, name="get_all_types"),
]