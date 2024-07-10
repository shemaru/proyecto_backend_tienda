from django.contrib import admin
from apps.products.models import *

class Unit_Of_MeasurementAdmin(admin.ModelAdmin):
    list_display = ('id','description')
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','description')

admin.site.register(Product)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Unit_Of_Measurement, Unit_Of_MeasurementAdmin)   
admin.site.register(Discount)
