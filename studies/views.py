from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Studies
from .serializers import StudiesSerializer


# Create your views here.
def custom_response( status, success, message, data = None ):
    return Response(
        {
            'status': status,
            'success': success,
            'message': message,
            'data': data
        }
    )


class StudiesList(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            studies = Studies.objects.all()
            serializer = StudiesSerializer(studies, many=True)
            return custom_response( status=status.HTTP_200_OK, success=True, message="Studies fetched successfully", data = serializer.data)
        except Studies.DoesNotExist:
            return custom_response( status=status.HTTP_404_NOT_FOUND, success=False, message="Studies not found")
    
    def post(self, request):
        serializer = StudiesSerializer(data=request.data)
        if serializer.is_valid():
            study = serializer.save()
            return custom_response( status=status.HTTP_201_CREATED, success=True, message="Study created successfully", data = serializer.data)
        return custom_response( status=status.HTTP_400_BAD_REQUEST, success=False, message="Study not created", data = serializer.errors)
    

class StudiesDetail(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            study = Studies.objects.get(pk=pk)
            serializer = StudiesSerializer(study)
            return custom_response( status=status.HTTP_200_OK, success=True, message="Study fetched successfully", data = serializer.data)
        except Studies.DoesNotExist:
            return custom_response( status=status.HTTP_404_NOT_FOUND, success=False, message="Study not found")
        

    def patch(self, request, pk):
        try:
            study = Studies.objects.get(pk=pk)
        except Studies.DoesNotExist:
            return custom_response( status=status.HTTP_404_NOT_FOUND, success=False, message="Study not found")
        serializer = StudiesSerializer(study, data=request.data , partial=True)
        if serializer.is_valid():
            serializer.save()
            return custom_response( status=status.HTTP_200_OK, success=True, message="Study updated successfully", data = serializer.data)
        return custom_response( status=status.HTTP_400_BAD_REQUEST, success=False, message="Study not updated", data = serializer.errors)
    

    def delete(self, request, pk):
        try:
            study = Studies.objects.get(pk=pk)
            study.delete()
            return custom_response( status=status.HTTP_204_NO_CONTENT, success=True, message="Study deleted successfully")
        except Studies.DoesNotExist:
            return custom_response( status=status.HTTP_404_NOT_FOUND, success=False, message="Study not found")
        