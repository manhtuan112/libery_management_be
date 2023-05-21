from django.shortcuts import render
from .serializers import UserRegisterSerializer, UserLoginSerializer
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from user_service.models import User
# Create your views here.


@api_view(["POST"])
def UserRegister(request):
    serializer = UserRegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.validated_data['password'] = make_password(
            serializer.validated_data['password'])
        serializer.save()

        return Response({
            'success': True,
            'code': 201,
            'message': 'Register successful!',
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)

    else:
        return Response({
            'success': False,
            'code': 400,
            'message': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def UserLogin(request):

    try:
        user = get_object_or_404(User, username=request.data.get(
            'username'))
        
        if check_password(request.data.get('password'), user.password):
            serializer = UserLoginSerializer(user, many=False)
            data = {
                'success': True,
                'code': 200,
                "message": "Login Successfull",
                'data': serializer.data}
            return Response(data, status=status.HTTP_200_OK)
        else: 
            return Response({
            'success': False,
            'code': 400,
            'message': 'Username or password is incorrect!',
        }, status=status.HTTP_400_BAD_REQUEST)

    except Exception:
        return Response({
            'success': False,
            'code': 400,
            'message': 'Username or password is incorrect!',
        }, status=status.HTTP_400_BAD_REQUEST)
