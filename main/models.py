from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=256, null=True)
    description = models.CharField(max_length=256, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.name

class ModifierGroup(models.Model):
    name = models.CharField(max_length=256, null=True)
    description = models.CharField(max_length=256, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Modifier(models.Model):
    name = models.CharField(max_length=256, null=True)
    price =  models.FloatField(null=True)
    modifier_group = models.ManyToManyField(ModifierGroup)
    description = models.CharField(max_length=256, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    STATUS = (
        ('Draft', 'Draft'),
        ('Published', 'Published'),
    )
    name = models.CharField(max_length=256, null=True)
    price =  models.FloatField(null=True)
    category = models.ManyToManyField(Category)
    description = models.CharField(max_length=256, null=True, blank=True)
    status = models.CharField(max_length=256, null=True, choices=STATUS)
    modifiers = models.ManyToManyField(ModifierGroup)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name



