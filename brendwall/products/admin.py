from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price')  # Поля, отображаемые в списке объектов
    search_fields = ('name', 'description')  # Поля для поиска
    list_filter = ('price',)  # Фильтрация по цене
    ordering = ('id',)  # Сортировка по ID


admin.site.register(Product, ProductAdmin)
