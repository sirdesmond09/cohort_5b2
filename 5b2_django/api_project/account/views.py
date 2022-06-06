from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomUserSerializer, LoginSerializer
from rest_framework.exceptions import NotFound
from django.contrib.auth import get_user_model
from rest_framework import mixins
from rest_framework import generics

from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login
from django.forms import model_to_dict

UserModel = get_user_model()

class UserList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = UserModel.objects.all()
    serializer_class = CustomUserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_password = serializer.validated_data.pop('password')
        serializer.validated_data['password'] = make_password(user_password)
    
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
        
        
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = CustomUserSerializer
    lookup_field = "id"
    
    
    

class LoginView(APIView):
    
    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                data = model_to_dict(user)
                return Response(data,status=status.HTTP_200_OK)
            else:
                return Response({"message":"Please activate your account to login"},status=status.HTTP_403_FORBIDDEN)
        else:
            return Response({"message":"Invalid username or password"},status=status.HTTP_401_UNAUTHORIZED)
    