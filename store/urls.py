from django.urls import path, include
from rest_framework_nested import routers
from . import views

# app_name = 'storefront'

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('collections', views.CollectionViewSet)
products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
products_router.register('reviews', views.ReviewViewSet, basename='product-review')
urlpatterns = [
    path('', include(router.urls)),
    path('', include(products_router.urls)),
    # path('collections/', views.CollectionList.as_view()),
    # path('products/<int:pk>', views.ProductViewSet.as_view()),
    # path('collections/<int:pk>', views.CollectionDetail.as_view(), name='collection-detail')

]
