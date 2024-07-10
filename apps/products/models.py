from django.db import models
from apps.base.models import BaseModel
from itertools import product

        
class Category(BaseModel):
    
    description = models.CharField("Categoria de Producto", max_length = 250, null=False, blank = False)
    
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        
    def __str__(self) -> str:
        return self.description
        
    
class Unit_Of_Measurement(BaseModel):
    
    description = models.CharField("Descripción", max_length = 250, null = True, blank = True)
    
    class Meta: 
        verbose_name = "Unidad de Medida"
        verbose_name_plural = "Unidades de Medida"
        
    def __str__(self) -> str:
        return self.description
    
    
class Discount(BaseModel):
    
    description = models.PositiveSmallIntegerField("Descuento", null = True, blank = True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, verbose_name = "Categoria del Descuento")
    
    def __str__(self) -> str:
        return f'Oferta en {self.category} : {self.description}%'
    
class Product(BaseModel):
    
    name = models.CharField("Nombre del Producto", max_length = 250, null = False, blank = False)
    description = models.CharField("Descripción de producto", max_length = 250, null = False, blank = False)
    image = models.ImageField('Imagen del Producto', upload_to='products/', blank=True, null=True)
    unit_of_measurement = models.ForeignKey(Unit_Of_Measurement, verbose_name = "Unidad de Medida", on_delete = models.CASCADE, null = False, blank=False)
    category = models.ForeignKey(Category, verbose_name= "Caterogia del producto", on_delete=models.CASCADE, null = False, blank=False)
    
    class Meta:        
        verbose_name = "Producto"
        verbose_name_plural = "Productos"    
        
    def __str__(self):
        return self.name
    
    @property
    def stock(self):
        from django.db.models import Sum
        from apps.expense_manager.models import Expense
        from apps.sales.models import Sales  

        expenses = Expense.objects.filter(
            product=self,
            state=True
        ).aggregate(total_expenses=Sum('quantity'))

        sales = Sales.objects.filter(
            product=self,
            state=True
        ).aggregate(total_sales=Sum('quantity'))

        total_expenses = expenses.get('total_expenses') or 0
        total_sales = sales.get('total_sales') or 0

        return total_expenses - total_sales
