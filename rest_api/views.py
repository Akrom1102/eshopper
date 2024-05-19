import datetime
from django.db.transaction import atomic
from django.shortcuts import render, redirect
from product.models import Category, Product, ClientComment, User
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CategorySerializer, ProductSerializer, ClientCommentSerializer, UserSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters, status, permissions
from rest_framework.pagination import LimitOffsetPagination


class CategoryDetailApiView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]
    # authentication_classes = (TokenAuthentication),
    # permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ['name', 'product_count']
    pagination_class = LimitOffsetPagination

    @action(detail=False, methods=['get'])
    def re_order(self, request, *args, **kwargs):
        categories = self.get_queryset()
        categories = categories.order_by('-id')
        serializer = CategorySerializer(categories, many=True)
        return Response(data=serializer.data)

    @action(detail=False, methods=['get'])
    def national_category(self, request, *args, **kwargs):
        categories = self.get_queryset()
        categories = categories.filter(national=True)
        serializer = CategorySerializer(categories, many=True)
        return Response(data=serializer.data)

    @action(detail=True, methods=['get'])
    def products_count(self, request, *args, **kwargs):
        categories = self.get_object()
        products = Product.objects.filter(category=categories)
        products = products.count()
        categories.product_count = products
        categories.save()
        return Response(data=products)


class ProductDetailApiView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
    # authentication_classes = (TokenAuthentication),
    # permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ['name', 'price']
    pagination_class = LimitOffsetPagination

    @action(detail=False, methods=['get'])
    def re_order(self, request, *args, **kwargs):
        products = self.get_queryset()
        products = products.order_by('-id')
        serializer = ProductSerializer(products, many=True)
        return Response(data=serializer.data)

    @action(detail=True, methods=['POST'])
    def listen(self, request, *args, **kwargs):
        product = self.get_object()
        with atomic():
            product.popular_products += 1
            product.save()
            return Response(status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'])
    def category(self, request, *args, **kwargs):
        products = self.get_object()
        category = products.category
        serializer = CategorySerializer(category)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class CommentsDetailApiView(ModelViewSet):
    queryset = ClientComment.objects.all()
    serializer_class = ClientCommentSerializer
    permission_classes = [permissions.AllowAny]
    # authentication_classes = (TokenAuthentication),
    # permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ['name', 'comment']
    pagination_class = LimitOffsetPagination

    @action(detail=True, methods=['get'])
    def users(self, request, *args, **kwargs):
        comment = self.get_object()
        users = comment.customer
        serializer = UserSerializer(users)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def comments_count(self, request, *args, **kwargs):
        comments = self.get_queryset()
        data = comments.count()
        return Response(data=data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def today_comment(self, request, *args, **kwargs):
        comments = self.get_queryset()
        comments = comments.filter(created_date__icontains=datetime.now().date())
        serializer = ClientCommentSerializer(comments, many=True)
        return Response(data=serializer.data)


class UserDetailApiView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    # authentication_classes = (TokenAuthentication),
    # permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ['first_name', 'last_name', 'username']
    pagination_class = LimitOffsetPagination
