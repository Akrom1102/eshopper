from django.db import models
from .helps import SaveMediaFiles


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=40)

    class Meta:
        ordering = ('id',)
        indexes = [
            models.Index(fields=['id'])
        ]

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Category(models.Model):
    image = models.ImageField(upload_to=SaveMediaFiles.category_image_path)
    name = models.CharField(max_length=50)
    product_count = models.IntegerField(default=1)

    class Meta:
        ordering = ('id',)
        indexes = [
            models.Index(fields=['id'])
        ]

    def __str__(self):
        return self.name


class PriceType(models.TextChoices):
    EURO = 'EURO', 'EURO'
    DOLLAR = '$', '$'
    SUM = 'SO`M', 'SO`M'


class Product(models.Model):
    image = models.ImageField(upload_to=SaveMediaFiles.product_image_path)
    name = models.CharField(max_length=25)
    price = models.IntegerField()
    price_type = models.CharField(max_length=4, choices=PriceType.choices)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        ordering = ('id',)
        indexes = [
            models.Index(fields=['id'])
        ]

    def __str__(self):
        return self.name


class ClientComment(models.Model):
    image = models.ImageField(upload_to=SaveMediaFiles.clientcomment_image_path)
    name = models.CharField(max_length=150)
    comment = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('id',)
        indexes = [
            models.Index(fields=['id'])
        ]

    def __str__(self):
        return self.name
