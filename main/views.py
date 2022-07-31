from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Category, Product, ModifierGroup, Modifier


#Products

class ProductCreate(CreateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('products')


class ProductUpdate(UpdateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('products')
class ProductList(ListView):
    model = Product
    context_object_name = 'products'
 

class ProductDetail(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'main/product.html'


#Categories

class CategoryCreate(CreateView):
    model = Category
    fields = '__all__'
    success_url = reverse_lazy('categories')

class CategoryUpdate(UpdateView):
    model = Category
    fields = '__all__'
    success_url = reverse_lazy('categories')

class CategoryList(ListView):
    model = Category
    context_object_name = 'categories'



#ModifierGroup

class MGCreate(CreateView):
    model = ModifierGroup
    fields = '__all__'
    success_url = reverse_lazy('modifiergroups')
    template_name = 'main/mg_form.html'


class MGUpdate(UpdateView):
    model = ModifierGroup
    fields = '__all__'
    success_url = reverse_lazy('modifiergroups')
    template_name = 'main/mg_form.html'

class MGList(ListView):
    model = ModifierGroup
    context_object_name = 'modifiergroups'
    template_name = 'main/modifiergroups_list.html'

#Modifiers

class ModifierCreate(CreateView):
    model = Modifier
    fields = '__all__'
    success_url = reverse_lazy('modifiers')
    template_name = 'main/modifier_form.html'


class ModifierUpdate(UpdateView):
    model = Modifier
    fields = '__all__'
    success_url = reverse_lazy('modifiers')
    template_name = 'main/modifier_form.html'

class ModifierList(ListView):
    model = ModifierGroup
    context_object_name = 'modifiers'
    template_name = 'main/modifier_list.html'

    
    



