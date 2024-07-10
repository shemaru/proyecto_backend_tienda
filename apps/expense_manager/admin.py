from django.contrib import admin

from apps.expense_manager.models import *

class SupplierAdmin(admin.ModelAdmin):
    list_display = ('id','business_name')
    
class Pay_MethodAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    
class ExpenseCategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('id')

admin.site.register(Supplier)
admin.site.register(Pay_Method)
admin.site.register(ExpenseCategory)
admin.site.register(Expense)
