from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response
from ..models import Product, Order
from ..serializers import ProductSerializer, OrderSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

@api_view(['GET'])
def get_all(request):
    #Get all the products
    products = Product.objects.all()
    
    # Serialize the products
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_product(request):
    # Set the creator of the product to the currently authenticated user
    request.data['created_by'] = request.user.id

    # Deserialize the request data using the BoardSerializer
    serializer = ProductSerializer(data=request.data)

    # Validate and save the data if valid
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_product(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({"error": "Product does not exist"}, status=status.HTTP_404_NOT_FOUND)

    # Check if the user has permission to update the product
    if product.created_by != request.user:
        return Response({"error": "You do not have permission to update this product"}, status=status.HTTP_403_FORBIDDEN)

    serializer = ProductSerializer(product, data=request.data)
    if serializer.is_valid():
        serializer.save(updated_by=request.user)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_product(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({"error": "Product does not exist"}, status=status.HTTP_404_NOT_FOUND)

    # Check if the user has permission to delete the product
    if product.created_by != request.user:
        return Response({"error": "You do not have permission to delete this product"}, status=status.HTTP_403_FORBIDDEN)

    product.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
