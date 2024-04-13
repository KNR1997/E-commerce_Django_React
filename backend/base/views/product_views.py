from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response
from ..models import Product, Order
from ..serializers import ProductSerializer, OrderSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.core.paginator import Paginator
from django.http import QueryDict

@api_view(['GET'])
def get_products(request):
    try:
        # Get query parameters
        query_params = request.query_params
        limit = int(query_params.get('limit', 30))
        page = int(query_params.get('page', 1))
        search = query_params.get('search')

        # Get all the products
        products = Product.objects.all()

        # Apply search filter
        # if search:
        #     search_filters = {}
        #     for param in search.split(';'):
        #         key, value = param.split(':')
        #         if key != 'slug':
        #             search_filters[key] = value
        #     products = products.filter(**search_filters)
        search_filters = {}
        for param in search.split(';'):
            key, value = param.split(':')
            if key == 'type.slug':  # Check if the key is 'type.slug'
                search_filters['type__slug'] = value  # Use '__' to traverse the relationship
            elif key != 'slug':
                search_filters[key] = value

        # Then apply the filters to the queryset
        products = products.filter(**search_filters)

        # Paginate results
        paginator = Paginator(products, limit)
        paginated_products = paginator.get_page(page)

        # Serialize the paginated products
        serializer = ProductSerializer(paginated_products, many=True)

        # Construct next page URL
        next_page_url = None
        if paginated_products.has_next():
            next_page_url = f"{request.path}?{query_params.urlencode()}&page={page + 1}"

        # Construct previous page URL
        previous_page_url = None
        if paginated_products.has_previous():
            previous_page_url = f"{request.path}?{query_params.urlencode()}&page={page - 1}"

        return Response({
            'data': serializer.data,
            'next': next_page_url,
            'previous': previous_page_url
        })

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
