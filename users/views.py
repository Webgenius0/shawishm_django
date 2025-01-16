from django.contrib.auth import authenticate
from .serializers import SignUpSerializer , ProfileSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


# Create your views here.

class SignUpView(APIView):

    permission_classes = []
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': status.HTTP_201_CREATED, 
                'success': True, 
                'message': 'User created successfully', 
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class SignInView(APIView):

    permission_classes = []

    def post(self, request):

        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            raise ValidationError({'error': ('Username and password are required')})
        
    
        user = authenticate(username=username, password=password)

        if user is not None:
            token = RefreshToken.for_user(user)

            return Response({
                'status': status.HTTP_200_OK,
                'success': True,
                'message': 'Login successful',
                'refresh': str(token),
                'access': str(token.access_token),
            }, status=status.HTTP_200_OK)
        
        return Response({
            'status': status.HTTP_401_UNAUTHORIZED,
            'success': False,
            'message': 'Invalid username or password',
        }, status=status.HTTP_401_UNAUTHORIZED)
    

class GetUserView(APIView):

    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        user = request.user
        serializer = ProfileSerializer(user)
        return Response({
            'status': status.HTTP_200_OK,
            'success': True,
            'message': 'User fetched successfully',
            'data': serializer.data
        }, status=status.HTTP_200_OK)
    
class UpdateUserView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        serializer = ProfileSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response({
                'status': status.HTTP_200_OK,
                'success': True,
                'message': 'User updated successfully',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'success': False,
            'message': 'User not updated',
            'data': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    

class ChangePasswordView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')
        confirm_password = request.data.get('confirm_password')

        if not old_password or not new_password or not confirm_password:
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'success': False,
                'message': 'All fields are required',
            }, status=status.HTTP_400_BAD_REQUEST)
        
        if new_password != confirm_password:
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'success': False,
                'message': 'New password and confirm password do not match',
            }, status=status.HTTP_400_BAD_REQUEST)
        
        if not user.check_password(old_password):
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'success': False,
                'message': 'Old password is incorrect',
            }, status=status.HTTP_400_BAD_REQUEST)
        
        user.set_password(new_password)
        user.save()

        return Response({
            'status': status.HTTP_200_OK,
            'success': True,
            'message': 'Password changed successfully',
        }, status=status.HTTP_200_OK)