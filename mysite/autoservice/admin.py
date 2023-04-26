from django.contrib import admin
from .models import (VehicleModel,
                     Service,
                     Vehicle,
                     Order,
                     OrderLine)

class OrderLineInline(admin.TabularInline):
    model = OrderLine
    extra = 0

class VehicleAdmin(admin.ModelAdmin):
    list_display = ['vehicle_model', 'owner_name', 'plate', 'vin']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['vehicle', 'date']
    inlines = [OrderLineInline]

# Register your models here.
admin.site.register(VehicleModel)
admin.site.register(Service)
admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderLine)
