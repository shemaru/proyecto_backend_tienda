from apps.products.models import *
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        exclude = ('state','created_date','modified_date','deleted_date')
        
#forma para serializar relaciones en modelos
    def to_representation(self, instance):
        stock = instance.stock  # Directamente obtenemos el stock calculado
        return {
            'id': instance.id,
            'stock': stock,
            'name': instance.name,            
            'description': instance.description,
            'image': instance.image.url if instance.image else '',
            'unit_of_measurement': instance.unit_of_measurement.description if instance.unit_of_measurement else '',
            'category': instance.category.description if instance.category else ''
        }

class ProductRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        exclude = ('state','created_date','modified_date','deleted_date')