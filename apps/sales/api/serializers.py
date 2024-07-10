from apps.sales.models import Sales
from rest_framework import serializers

class SalesSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Sales
        exclude = ('state','created_date','modified_date','deleted_date','time_field')   
        
    def to_representation(self, instance):
            return {
            'id': instance.id,
            'date': instance.date, 
            'time_field':instance.time_field,   
            'quantity': instance.quantity,    
            'product': instance.product.description 
        }
        
class RetrieveSalesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Sales
        exclude = ('state','created_date','modified_date','deleted_date')
       
    def to_representation(self, instance):
            return {
            'id': instance.id,
            'date': instance.date, 
            'time_field':instance.time_field,   
            'quantity': instance.quantity,    
            'product': instance.product.description 
        }