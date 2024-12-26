from django.contrib import admin
from .models import Category, SubCategory, Product

admin.site.register(Category)
admin.site.register(SubCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'date_added']
    list_filter = ['name', 'description', 'price']
    search_fields = ['name']

