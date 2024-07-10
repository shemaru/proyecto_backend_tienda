from apps.users.api.serializers import CustomTokenPairSerializer, CustomUserSerializer
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

# Vista para el login
class Login(TokenObtainPairView):
    serializer_class = CustomTokenPairSerializer
            
    def post(self, request, *args, **kwargs):
        username = request.data.get('username','')
        password = request.data.get('password','')
        user = authenticate(
            username = username,
            password = password            
        )
        
        if user:
            login_serializer = self.serializer_class(data=request.data)
            if login_serializer.is_valid():
                user_serializer = CustomUserSerializer(user)
                return Response({
                    'token': login_serializer.validated_data.get('access'),
                    'token-refresh': login_serializer.validated_data.get('refresh'),
                    'user': user_serializer.data,
                    'message':'¡Inicio de sesión exitoso!'},status=status.HTTP_200_OK)
            return Response({'error': 'Contraseña u nombre de usuario incorrectos'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Contraseña o nombre de usuario incorrectos'}, status=status.HTTP_400_BAD_REQUEST)
    
# Vista para el logout    
class Logout(APIView):
    permission_classes = (IsAuthenticated,)
    
    def post(self,request,*args, **kwargs):
        try:
            refresh_token = request.data('refresh')
            token = RefreshToken(refresh_token)
            token.blacklist()
            
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
