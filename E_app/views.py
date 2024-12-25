from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView, ListView
from .models import Category, SubCategory


def add_category(request):
    if request.method == "POST":
        name = request.POST.get('name')
        en = Category.objects.create(name=name)
        en.save()
        messages.success(request, 'Category added successfully')

    return render(request, 'E_shop/add_category.html')


class CategoryListView(ListView):
    model = Category
    template_name = 'E_shop/category_list.html'
    context_object_name = 'categories'

    def get_queryset(self):
        queryset = Category.objects.all()
        name = self.request.GET.get('category')

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset


def Add_SubCategory(request):
    category = Category.objects.all()

    context = {
        'categories': category
    }

    if request.method == 'POST':
        name = request.POST.get('name')
        category_id = request.POST.get('category')

        try:
            category = Category.objects.get(pk=category_id)
            SubCategory.objects.create(category=category, name=name)
            messages.success(request, 'Sub Category added successfully')
        except Category.DoesNotExist:
            messages.error(request, 'Category does not exist')
            return render(request, 'E_shop/add_category.html')

    return render(request, 'E_shop/add_subcategory.html', context)


def Sub_Category(request):
    subcategory = SubCategory.objects.all()

    context = {
        'subcategories': subcategory
    }
    return render(request, 'E_shop/sub_category.html', context)




