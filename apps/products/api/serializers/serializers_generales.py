from apps.products.models import Category, Discount, Unit_Of_Measurement
from rest_framework import serializers
   
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ('state','created_date','modified_date','deleted_date')
    
class DiscountReturnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        exclude = ('state','created_date','modified_date','deleted_date')   
        
        def to_representation(self, instance):
            return {
            'id': instance.id,
            'description': instance.description,
            'category': instance.category.__str__()
        }
            
class DiscountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Discount
        exclude = ('state','created_date','modified_date','deleted_date')      
        
class Unit_Of_MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit_Of_Measurement
        exclude = ('state','created_date','modified_date','deleted_date')