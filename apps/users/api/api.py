from apps.users.models import Usuario
from apps.users.api.serializers import(
    UserListSerializer, UserSerializer, 
    UpdatedSerializer, PasswordSerializer
)
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

class UsuarioViewSet(viewsets.GenericViewSet):
    model = Usuario
    serializer_class = UserSerializer
    serializer_list = UserListSerializer
    queryset = None
    
    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)
    
    def get_queryset(self):
        if self.queryset is None:
            self.queryset = self.model.objects\
                            .filter(is_active=True)\
                            .values('id', 'username', 'email', 'name')
        return self.queryset  
    
    @action(detail=True,methods=['post'])
    def set_password(self,request,pk=None):
        user = self.get_object(pk)
        user_serializer = PasswordSerializer(data=request.data)
        if user_serializer.is_valid():
            user.set_password(user_serializer.validated_data['password'])
            user.save()
            return Response({
                'message': 'Contraseña actualizada correctamente'
            })
        return Response({
            'message': 'Hay errores en la información enviada',
            'errors': user_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
        
    def list(self, request):
        users = self.get_queryset()
        users_serializer = self.serializer_list(users, many = True)
        return Response(users_serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        user_serializer = self.serializer_class(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({'message':'Usuario creado correctamente'},status=status.HTTP_200_OK)
        return Response({'message':'Hay errores en el registro','errors':user_serializer.errors},status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        user = self.get_object(pk)
        user_serializer = self.serializer_class(user)
        return Response(user_serializer.data)
    
    def update(self, request, pk=None):
        user = self.get_object(pk)
        user_serializer = UpdatedSerializer(user, data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({'message':'¡Datos actualizados correctamente!'},status=status.HTTP_200_OK)
        return Response({'message':'Hay errores en la actualización'},status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        user = self.get_object(pk)
        user.delete()
        return Response({'message':'¡Usuario eliminado correctamente!'},status=status.HTTP_204_NO_CONTENT)