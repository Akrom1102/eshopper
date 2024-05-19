from rest_framework import serializers
from product.models import Category, Product, ClientComment, User


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['name', 'product_count']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['name', 'price', 'description']


class ClientCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientComment
        fields = '__all__'
        read_only_fields = ['name', 'comment', 'product']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        read_only_fields = ['first_name', 'last_name', 'username']
