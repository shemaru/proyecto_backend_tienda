from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from apps.sales.api.serializers import *


class SalesViewSet(viewsets.GenericViewSet):
    serializer_class = SalesSerializer
    
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        return self.get_serializer().Meta.model.objects.filter(id=pk, state=True).first()

    def list(self, request):
        sales = self.get_queryset()
        sales_serializer = self.serializer_class(sales, many = True)
        return Response(sales_serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        sales_serializer = self.serializer_class(data=request.data)
        if sales_serializer.is_valid():
            sales_serializer.save()
            return Response({'message':'¡Venta Registrada!'},status=status.HTTP_201_CREATED)
        return Response({'message':'','error':sales_serializer.errors},status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        sale = self.get_queryset(pk)
        if sale:
            sale_serializer = RetrieveSalesSerializer(sale)
            return Response(sale_serializer.data, status=status.HTTP_200_OK)
        return Response({'message':'¡No existe un venta con esos datos! '},status=status.HTTP_400_BAD_REQUEST)
        
    def update(self,request, pk=None):
        sale = self.get_queryset(pk)
        sale_serializer = self.serializer_class(sale, data=request.data)
        if sale_serializer.is_valid():
            sale_serializer.save()
            return Response({'message':'Venta actualizada correctamente'},status=status.HTTP_200_OK)
        return Response({'message':'','error':sale_serializer.errors},status=status.HTTP_400_BAD_REQUEST)        

    def destroy(self, request, pk=None):
        sale = self.get_queryset().filter(id=pk).first()
        if sale:
            sale.state = False
            sale.save()
            return Response({'message':'¡Venta eliminada correctamente!'}, status=status.HTTP_200_OK)
        return({'message':'¡No existe una venta con esos datos!'}, status.HTTP_400_BAD_REQUEST)