from django.urls import path
from .views import ShopPageView, ContactPageView, CartView, CheckoutView, ProductDetail, ProductUpdateView, DeleteProductView, AdminPageView

urlpatterns = [
    path('shop', ShopPageView.as_view(), name='shop'),
    path('contact', ContactPageView.as_view(), name='contact'),
    path('shop/detail/cart/', CartView.as_view(), name='cart'),
    path('shop/detail/cart/checkout/', CheckoutView.as_view(), name='checkout'),
    path('shop/detail/<int:id>', ProductDetail.as_view(), name='detail'),
    path('shop/admin', AdminPageView.as_view(), name='admin-page'),
    path('shop/admin/update/<int:id>', ProductUpdateView.as_view(), name='product-update'),
    path('shop/admin/delete/<int:id>', DeleteProductView.as_view(), name='product-delete')
]