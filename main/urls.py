from django.urls import path
from .views import CategoryList, CategoryUpdate, CategoryCreate, ProductList, ProductDetail, ProductCreate, ProductUpdate, MGCreate, MGList, MGUpdate
from .views import ModifierCreate, ModifierList, ModifierUpdate
urlpatterns = [
    path('products/', ProductList.as_view(), name='products'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product'),
    path('product-create/', ProductCreate.as_view(), name='product-create'),
    path('product-update/<int:pk>/', ProductUpdate.as_view(), name='product-update'),

    path('categories/', CategoryList.as_view(), name='categories'),
    path('category-create/', CategoryCreate.as_view(), name='category-create'),
    path('category-update/<int:pk>/', CategoryUpdate.as_view(), name='category-update'),

    path('mg/', MGList.as_view(), name='modifiergroups'),
    path('mg-create/', MGCreate.as_view(), name='mg-create'),
    path('mg-update/<int:pk>/', MGUpdate.as_view(), name='mg-update'),

    path('modifiers/', ModifierList.as_view(), name='modifiers'),
    path('modifier-create/', ModifierCreate.as_view(), name='modifier-create'),
    path('modifier-update/<int:pk>/', ModifierUpdate.as_view(), name='modifier-update'),

]