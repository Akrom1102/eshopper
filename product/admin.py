from django.contrib import admin
from .models import Category, Product, User, ClientComment
from import_export.admin import ImportExportModelAdmin


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'product_count')
    list_display_links = ('id', 'name', 'product_count')
    search_fields = ('name', 'price')
    ordering = ('id',)


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'price', 'category')
    list_display_links = ('id', 'name', 'price', 'category')
    search_fields = ('name', 'price', 'category')
    ordering = ('id',)


@admin.register(User)
class UserAdmin(ImportExportModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'username')
    list_display_links = ('id', 'first_name', 'last_name', 'username')
    search_fields = ('first_name', 'last_name', 'username')
    ordering = ('id',)


@admin.register(ClientComment)
class ClientCommentAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'comment', 'product')
    list_display_links = ('id', 'name', 'comment', 'product')
    search_fields = ('name', 'comment', 'product')
    ordering = ('id',)
