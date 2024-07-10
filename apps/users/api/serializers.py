from rest_framework import serializers
from apps.users.models import Usuario
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenPairSerializer(TokenObtainPairSerializer):
    pass

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('username','email','name','last_name')
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        
    def create(self, validated_data):
        user = Usuario(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class UpdatedSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Usuario
        fields = ('username','email','name','last_name')
    
class PasswordSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=128, min_length=6, write_only = True)
    password2 = serializers.CharField(max_length=128, min_length=6, write_only = True) 
    
    def validate(self,data):
        if ['password1'] != ['password2']:
            raise serializers.ValidationError({'password':'Debe ingresar ambas contraseñas iguales'})
        return data        
           
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
    
    def to_representation(self, instance):
        return {
                'id': instance['id'],
                'username': instance['username'],
                'email': instance['email'],
                'name': instance['name']
        }                       
        