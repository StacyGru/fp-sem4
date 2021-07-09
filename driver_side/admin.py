from django.contrib import admin

# Register your models here.

from .models import Driver, ModelDetail, Car, Street, AvailableCar

from import_export.admin import ImportExportActionModelAdmin

class DriverAdmin(ImportExportActionModelAdmin):
    list_display = ('id', 'full_name', 'phone', 'gender')
    list_filter = ('gender',)
    search_fields = ('id', 'full_name', 'phone')

class ModelDetailAdmin(ImportExportActionModelAdmin):

    list_display = ('id', 'model', 'gearbox', 'seats', 'fuel_volume', 'wheel_side', 'child_seat')
    list_filter = ('seats', 'child_seat')
    search_fields = ('id', 'model')

class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'model', 'number', 'color', 'car_class')
    list_filter = ('brand', 'color', 'car_class')
    search_fields = ('id', 'model', 'number')

class CarAdmin(ImportExportActionModelAdmin):
    list_display = ('id', 'brand', 'model', 'number', 'color', 'car_class')
    list_filter = ('brand', 'color', 'car_class')
    search_fields = ('id', 'model', 'number')

class StreetAdmin(ImportExportActionModelAdmin):
    list_display = ('id', 'street', 'area')
    list_filter = ('area',)
    search_fields = ('id', 'street')

class AvailableCarAdmin(ImportExportActionModelAdmin):
    list_display = ('id', 'car_number', 'driver', 'street')
    list_filter = ('street',)
    search_fields = ('id', 'car_number', 'driver')

admin.site.register(Driver, DriverAdmin)
admin.site.register(ModelDetail, ModelDetailAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Street, StreetAdmin)
admin.site.register(AvailableCar, AvailableCarAdmin)