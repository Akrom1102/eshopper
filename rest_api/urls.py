from django.urls import path, include
from .views import CategoryDetailApiView, ProductDetailApiView, CommentsDetailApiView
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Shopper APi",
        description="Shopper Application demo",
        default_version="v1",
        terms_of_service='demo.com',
        contact=openapi.Contact(email='eshop@gmail.com'),
        license=openapi.License(name='demo service')
    ),
    public=True,
    permission_classes=[permissions.AllowAny, ]
)

router = routers.DefaultRouter()
router.register('category', CategoryDetailApiView, basename='category')
router.register('product', ProductDetailApiView, basename='product')
router.register('comment', CommentsDetailApiView, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
    path('docs-swagger/', schema_view.with_ui("swagger", cache_timeout=0), name='swagger'),
    path('docs-redoc/', schema_view.with_ui("redoc", cache_timeout=0), name='redoc'),
]
