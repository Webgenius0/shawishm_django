from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import RadiologyGroup
from .serializers import RadiologyGroupSerializer


# Create your views here.
class RadiologyGroupList(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        radiologyGroup = RadiologyGroup.objects.all()
        serializer = RadiologyGroupSerializer(radiologyGroup, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = RadiologyGroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class RadiologyGroupDetail(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            radiologyGroup = RadiologyGroup.objects.get(pk=pk)
            serializer = RadiologyGroupSerializer(radiologyGroup)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except RadiologyGroup.DoesNotExist:
            return Response({'error': 'Radiology Group not found'}, status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, pk):
        try:
            radiologyGroup = RadiologyGroup.objects.get(pk=pk)
            serializer = RadiologyGroupSerializer(radiologyGroup, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except RadiologyGroup.DoesNotExist:
            return Response({'error': 'Radiology Group not found'}, status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request, pk):
        try:
            radiologyGroup = RadiologyGroup.objects.get(pk=pk)
            radiologyGroup.delete()
            return Response({'success': 'Radiology Group deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except RadiologyGroup.DoesNotExist:
            return Response({'error': 'Radiology Group not found'}, status=status.HTTP_404_NOT_FOUND)