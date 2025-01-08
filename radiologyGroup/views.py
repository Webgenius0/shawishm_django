from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import RadiologyGroup
from .serializers import RadiologyGroupSerializer


# Create your views here.

def custom_response(status, success , message , data = None):
    return Response(
        {
            'status': status,
            'success': success,
            'message': message,
            'data': data
        }
    )

class RadiologyGroupList(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            radiologyGroup = RadiologyGroup.objects.all()
            serializer = RadiologyGroupSerializer(radiologyGroup, many=True)
            return custom_response( status=status.HTTP_200_OK, success=True, message="Radiology Groups fetched successfully", data = serializer.data)
        except RadiologyGroup.DoesNotExist:
            return custom_response( status=status.HTTP_404_NOT_FOUND, success=False, message="Radiology Groups not found")

    def post(self, request):
        serializer = RadiologyGroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return custom_response( status=status.HTTP_201_CREATED, success=True, message="Radiology Group created successfully", data = serializer.data)
        return custom_response( status=status.HTTP_400_BAD_REQUEST, success=False, message="Radiology Group not created", data = serializer.errors)
    

class RadiologyGroupDetail(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            radiologyGroup = RadiologyGroup.objects.get(pk=pk)
            serializer = RadiologyGroupSerializer(radiologyGroup)
            return custom_response( status=status.HTTP_200_OK, success=True, message="Radiology Group fetched successfully", data = serializer.data)
        except RadiologyGroup.DoesNotExist:
            return custom_response( status=status.HTTP_404_NOT_FOUND, success=False, message="Radiology Group not found")
        
    def put(self, request, pk):
        try:
            radiologyGroup = RadiologyGroup.objects.get(pk=pk)
            serializer = RadiologyGroupSerializer(radiologyGroup, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return custom_response( status=status.HTTP_200_OK, success=True, message="Radiology Group updated successfully", data = serializer.data)
            return custom_response( status=status.HTTP_400_BAD_REQUEST, success=False, message="Radiology Group not updated", data = serializer.errors)
        except RadiologyGroup.DoesNotExist:
            return custom_response( status=status.HTTP_404_NOT_FOUND, success=False, message="Radiology Group not found")
        
    def delete(self, request, pk):
        try:
            radiologyGroup = RadiologyGroup.objects.get(pk=pk)
            radiologyGroup.delete()
            return custom_response( status=status.HTTP_204_NO_CONTENT, success=True, message="Radiology Group deleted successfully")
        except RadiologyGroup.DoesNotExist:
            return custom_response( status=status.HTTP_404_NOT_FOUND, success=False, message="Radiology Group not found")