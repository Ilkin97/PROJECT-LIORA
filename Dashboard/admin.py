from django.contrib import admin
from .models import Product, Task, Order

# Register your models here.

# Header, title and index title settings
admin.site.site_header = "Liora Admin"
admin.site.site_title = "Liora Admin Panel"
admin.site.index_title = "Welcome, Admin!"

# Product model admin settings
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'volume', 'gender', 'in_stock', 'stock_quantity', 'on_sale', 'discount_percentage', 'discount_price')
    list_filter = ('gender', 'on_sale', 'volume')
    search_fields = ('name', 'description')
    
    class Media:
        js = ('js/product_discount.js',)

    def save_model(self, request, obj, form, change):
        if obj.discount_percentage:
            obj.discount_price = obj.price - (obj.price * obj.discount_percentage / 100)
        else:
            obj.discount_price = obj.price
        super().save_model(request, obj, form, change)

# Register models
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(Task)