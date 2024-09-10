from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from .models import Product
from .serializers import ProductSerializer
from django.shortcuts import render


def product_form(request):
    return render(request, 'products/product_form.html')


def product_list(request):
    return render(request, 'products/product_list.html')


@api_view(['POST'])
def create_product(request):
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_products(request):
    if request.method == 'GET':
        # Фильтрация продуктов по названию, описанию и цене
        name = request.GET.get('name', '')
        description = request.GET.get('description', '')
        min_price = request.GET.get('min_price')
        max_price = request.GET.get('max_price')

        products = Product.objects.all()
        if name:
            products = products.filter(name__icontains=name)
        if description:
            products = products.filter(Q(description__icontains=description))
        if min_price is not None:
            products = products.filter(price__gte=min_price)
        if max_price is not None:
            products = products.filter(price__lte=max_price)

        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
