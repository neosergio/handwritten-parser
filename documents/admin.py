from django.contrib import admin
from .models import Document, Product


class DocumentAdmin(admin.ModelAdmin):
    list_display = ('text', 'date_added')
    search_fields = ['text']


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']


admin.site.register(Document, DocumentAdmin)
admin.site.register(Product, ProductAdmin)
