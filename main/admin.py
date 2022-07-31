from django.contrib import admin

from .models import Category, Product, ModifierGroup, Modifier

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ModifierGroup)
admin.site.register(Modifier)
