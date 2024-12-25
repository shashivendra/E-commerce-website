from django.contrib.auth.decorators import login_required
from django.urls import path, include
from .views import *
from .dashboard_views import register, login, master, SuperAdminDashboardView, index


urlpatterns = [
    path('add-category/', add_category, name='add_category'),
    path('category-list/', CategoryListView.as_view(), name='category_list'),
    path('add-subcategory/', Add_SubCategory, name='add_subcategory'),
    path('sub-category/', Sub_Category, name='sub_category'),

]

urlpatterns += [
    # path('', master, name='master'),
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('super-admin-dashboard/', SuperAdminDashboardView.as_view(), name='super_admin_dashboard'),
]