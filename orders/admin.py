from django.contrib import admin

from .models import Order, ReciverInfo


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ('id', 'user', 'code',
                    'total_price', 'shipping_status', 'created_at')
    list_display_links = ('id', 'user')
    list_editable = ('shipping_status',)
    list_filter = ('shipping_status', 'purchase_invoice', 'created_at')
    list_per_page = 25
    search_fields = ('user__phone_number', 'user__email', 'code')
    readonly_fields = ('code',)

    def total_price(self, obj):
        return str(obj.cart.total_price) + "$"


@admin.register(ReciverInfo)
class ReciverInfoAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ('id', 'full_name', 'phone_number', 'address', 'created_at')
    list_display_links = ('id', 'full_name')
    list_filter = ('created_at',)
    list_per_page = 25
    search_fields = ('full_name', 'phone_number', 'address')
    readonly_fields = ('full_name', 'phone_number', 'address')
