from django.views import View
from django.shortcuts import render
from .models import Product


class ProductListView(View):
    def get(self, request):
        category = request.GET.get('category')
        brand = request.GET.get('brand')
        warranty = request.GET.get('warranty')
        is_liked = request.GET.get('is_liked')
        min_price = request.GET.get('min_price')
        max_price = request.GET.get('max_price')

        products = Product.objects.all()

        if category:
            products = products.filter(category=category)

        if brand:
            products = products.filter(brand=brand)

        if warranty:
            products = products.filter(warranty=warranty)

        if is_liked:
            products = products.filter(is_liked=True)

        if min_price and max_price:
            products = products.filter(price__gte=min_price, price__lte=max_price)

        # Retrieve available filter options
        product_categories = Product.objects.values_list('category', flat=True).distinct()
        product_brands = Product.objects.values_list('brand', flat=True).distinct()
        product_warranties = Product.objects.values_list('warranty', flat=True).distinct()

        return render(request, 'product_list.html', {
            'products': products,
            'product_categories': product_categories,
            'product_brands': product_brands,
            'product_warranties': product_warranties,
        })
