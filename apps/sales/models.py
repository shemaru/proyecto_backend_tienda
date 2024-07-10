from django.db import models
from apps.base.models import BaseModel
from apps.products.models import Product
from django.dispatch import receiver
from django.db.models.signals import post_save

class Sales(BaseModel):
    
    date = models.DateField("Fecha", max_length = 20, auto_now = False, auto_now_add = False)
    time_field = models.TimeField("Horario",auto_now=True,auto_now_add=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.DecimalField('Cantidad', max_digits=10, decimal_places=2)

    class Meta:        
        
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"  
        
    def __str__(self):
        return self.date
