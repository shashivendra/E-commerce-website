from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages

from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView

from .models import Category, SubCategory, Product


def register(request):
    if request.method == "POST":
        user_name = request.POST.get('user_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password == password2:
            if User.objects.filter(username=user_name).exists():
                messages.error(request, 'User with this name already exists')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email with this name already exists')
            else:
                user = User.objects.create_user(username=user_name, email=email, password=password)
                user.save()
                return redirect('login')


        else:
            messages.error(request, 'Passwords do not match')
    return render(request, 'E_shop/register.html')


def login(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')

        user = authenticate(request, username=user_name, password=password)
        if user is not None:
            auth_login(request, user)
            if user.is_superuser:
                return redirect(reverse('super_admin_dashboard'))
            else:
                return redirect('index')

        else:
            return redirect('index')

    return render(request, 'E_shop/login.html')


class SuperAdminDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'E_shop/super_admin_dashboard.html'


def master(request):
    category = Category.objects.all()
    context = {
        'categories': category,

    }
    return render(request, 'E_shop/master.html', context)


def index(request):
    category = Category.objects.all()
    product = Product.objects.all()
    context = {
         'categories': category,
         'products': product,

     }

    return render(request, 'E_shop/index.html', context)