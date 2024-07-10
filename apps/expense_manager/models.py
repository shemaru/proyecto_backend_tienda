from django.db import models
from apps.base.models import BaseModel
from apps.products.models import Product
from apps.users.models import Usuario

class Supplier(BaseModel):
    
    ruc = models.CharField(unique=True, max_length=20)
    business_name = models.CharField("Nombre de proveedor", max_length=250, unique=True)
    address = models.CharField("Dirección", max_length=250, null=True)
    phone = models.CharField("Número de telefono", max_length=250, blank=True, null=True)
    email = models.EmailField("Email", max_length=254, null=True)
    
    class Meta:
        
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
        
    def to_dict(self):
        return {
            'id': self.id,
            'ruc': self.ruc,
            'business_name': self.business_name,
            'address': self.address,
            'phone': self.phone,
            'email': self.email
        }
        
    def __str__(self):
        return self.business_name
    
class Pay_Method(BaseModel):
    
    name = models.CharField("Método de pago", max_length=250)
    
    class Meta:
        
        verbose_name = "Método de pago"
        verbose_name_plural = "Método de pagos"
    
    def __str__(self):
        return self.name
    
class ExpenseCategory(BaseModel):
    name = models.CharField('Nombre de Categoría de Gasto', max_length=100)

    class Meta:
        ordering = ['id']
        verbose_name = 'Categoria de Gasto'
        verbose_name_plural = 'Categorias de Gastos'

    def __str__(self):
        return self.name
              
class Expense(BaseModel):
    
    date = models.DateField("Fecha", max_length = 20, auto_now = False, auto_now_add = False)
    quantity = models.DecimalField('Cantidad', max_digits=10, decimal_places=2)
    unit_price = models.DecimalField('Precio Unitario', max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField('Total', max_digits=10, decimal_places=2, default=0)
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    pay_method = models.ForeignKey(Pay_Method, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    class Meta:        
        ordering = ['id']
        verbose_name = "Gasto"
        verbose_name_plural = "Gastos"  
        
    def __str__(self):
        return self.date
