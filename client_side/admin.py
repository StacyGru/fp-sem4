from django.contrib import admin

# Register your models here.

from .models import Client, Operator, Order, Ride, DiscountCard

from import_export.admin import ImportExportActionModelAdmin

def order_is_done(modeladmin, request, queryset):
    queryset.update(status='завершён')
order_is_done.short_description = "Change the status of order to 'done'"

class ClientAdmin(ImportExportActionModelAdmin):
    list_display = ('id', 'full_name', 'phone', 'gender', 'login', 'password')
    list_filter = ('gender',)
    search_fields = ('id', 'full_name', 'phone', 'login')

class OperatorAdmin(ImportExportActionModelAdmin):
    list_display = ('id', 'full_name', 'phone', 'gender')
    list_filter = ('gender',)
    search_fields = ('id', 'full_name')

class OrderAdmin(ImportExportActionModelAdmin):
    list_display = ('id', 'client', 'operator', 'order_time', 'status', 'from_place', 'to_place', 'car_class',
                    'driver_gender')
    list_filter = ('operator', 'order_time', 'status', 'car_class', 'driver_gender')
    search_fields = ('id', 'client', 'order_time', 'from_place', 'to_place')
    list_editable = ('status',)
    actions = [order_is_done]

class RideAdmin(ImportExportActionModelAdmin):
    list_display = ('id', 'order', 'duration', 'mileage', 'price', 'car_id', 'driver')
    list_filter = ('car_id', 'driver')
    search_fields = ('id', 'order', 'duration', 'mileage', 'price')

class DiscountCardAdmin(ImportExportActionModelAdmin):
    list_display = ('id', 'client', 'points')
    search_fields = ('id', 'client', 'points')

admin.site.register(Client, ClientAdmin)
admin.site.register(Operator, OperatorAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Ride, RideAdmin)
admin.site.register(DiscountCard, DiscountCardAdmin)