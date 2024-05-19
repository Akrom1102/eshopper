from django.shortcuts import render, redirect
from django.views import View
from .models import Category, Product, ClientComment
from django.contrib.auth.mixins import LoginRequiredMixin


class ShopPageView(LoginRequiredMixin, View):
    def get(self, request):
        search = request.GET.get('search')
        category = Category.objects.all()
        products = Product.objects.all()
        client_comments = ClientComment.objects.all()
        if not search:
            context = {
                'category': category,
                'products': products,
                'client_comments': client_comments,
                'search': search
            }
            return render(request, 'shop.html', context)
        else:
            products = Product.objects.filter(name__icontains=search)
            if products:
                context = {
                    'category': category,
                    'products': products,
                    'client_comments': client_comments,
                    'search': search
                }
                return render(request, 'shop.html', context)
            else:
                context = {
                    'category': category,
                    'products': products,
                    'client_comments': client_comments,
                    'search': search
                }
                return render(request, 'shop.html', context)


class ContactPageView(LoginRequiredMixin, View):
    def get(self, request):
        category = Category.objects.all()
        products = Product.objects.all()
        client_comments = ClientComment.objects.all()
        context = {
            'category': category,
            'products': products,
            'client_comments': client_comments,
        }
        return render(request, 'contact.html', context)


class ProductDetail(LoginRequiredMixin, View):
    def get(self, request, id):
        products = Product.objects.get(id=id)
        client_comments = ClientComment.objects.all()
        return render(request, 'detail.html', {'products': products, 'client_comments': client_comments})


class AdminPageView(LoginRequiredMixin, View):
    def get(self, request):
        products = Product.objects.all()
        client_comments = ClientComment.objects.all()
        return render(request, 'adminpage.html', {'products': products, 'client_comments': client_comments})


class CartView(LoginRequiredMixin, View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'cart.html', {'products': products})


class CheckoutView(LoginRequiredMixin, View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'checkout.html', {'products': products})


# Update and deletes
class ProductUpdateView(LoginRequiredMixin, View):
    def get(self, request, id):
        products = Product.objects.get(id=id)
        return render(request, 'product_update.html', {'products': products})

    def post(self, request, id):
        product = Product.objects.get(id=id)
        product.name = request.POST['name']
        product.price = request.POST['price']
        product.price_type = request.POST['price_type']
        product.description = request.POST['description']

        product.save()
        return redirect("admin-page")


class DeleteProductView(View):
    def get(self, request, id):
        product = Product.objects.get(id=id)
        product.delete()
        return redirect("admin-page")
