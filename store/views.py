from django.db.models import Count
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from .filters import ProductFilter
from .models import Product, Collection, OrderItem, Review
from .pagination import DefaultPagination
from .serializers import ProductSerializer, CollectionSerializer, ReviewSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.select_related('collection').all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    pagination_class = DefaultPagination
    search_fields = ['title', 'description']
    ordering_fields = ['unit_price', 'last_update']

    # def get_queryset(self):
    #     queryset = Product.objects.select_related('collection').all()
    #     collection_id = self.request.query_params.get('collection_id', None)
    #     if collection_id is not None:
    #         queryset = queryset.filter(collection_id=collection_id)
    #     return queryset

    def get_serializer_context(self):
        context = {'request': self.request}
        return context

    def destroy(self, request, *arg, **kwargs):
        if OrderItem.objects.filter(product_id=kwargs['pk']).count() > 0:
            return Response({'error': 'Product cannot be deleted cause it has an order item'},
                            status=status.HTTP_405_METHOD_NOT_ALLOWED)

        return super().destroy(request, *arg, **kwargs)


class CollectionViewSet(ModelViewSet):
    serializer_class = CollectionSerializer
    queryset = Collection.objects.annotate(product_count=Count('products')).all()

    def get_serializer_context(self):
        context = {'request': self.request}
        return context

    def destroy(self, request, *arg, **kwargs):
        collection = get_object_or_404(Collection, pk=kwargs['pk'])
        if collection.products.count() > 0:
            return Response({'error': 'Collection cannot be deleted cause it has an featured product'},
                            status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().destroy(request, *arg, **kwargs)


class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs['product_pk'])

    def get_serializer_context(self):
        return {'product_id': self.kwargs['product_pk']}
