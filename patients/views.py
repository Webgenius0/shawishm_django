from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Patients
from .serializers import PatientsSerializer


# Create your views here.

def custom_response( success , message, data=None, status=status.HTTP_200_OK):
    return Response(
            {
            'status': status,
            'success': success,
            'message': message,
            'data': data
        }
    )


class PatientList(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            patients = Patients.objects.all()
            serializer = PatientsSerializer(patients, many=True)
            return custom_response( status=status.HTTP_200_OK, success=True, message="Patients fetched successfully", data = serializer.data)
        except Patients.DoesNotExist:
            return custom_response( status=status.HTTP_404_NOT_FOUND, success=False, message="Patients not found")
        
    
    def post(self, request):
        serializer = PatientsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return custom_response(status=status.HTTP_201_CREATED, success=True, message="Patient created successfully", data = serializer.data)
        return custom_response( status=status.HTTP_400_BAD_REQUEST, success=False, message="Patient not created", data = serializer.errors)

class PatientDetail(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            patient = Patients.objects.get(pk=pk)
            serializer = PatientsSerializer(patient)
            return custom_response( status=status.HTTP_200_OK, success=True, message="Patient fetched successfully", data = serializer.data)
        except Patients.DoesNotExist:
            return custom_response( status=status.HTTP_404_NOT_FOUND, success=False, message="Patient not found")

    def put(self, request, pk):
        patient = Patients.objects.get(pk=pk)
        serializer = PatientsSerializer(patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return custom_response( status=status.HTTP_200_OK, success=True, message="Patient updated successfully", data = serializer.data)
        return custom_response( status=status.HTTP_400_BAD_REQUEST, success=False, message="Patient not updated", data = serializer.errors)
    
    def delete(self, request, pk):
        patient = Patients.objects.get(pk=pk)
        patient.delete()
        return custom_response( status=status.HTTP_204_NO_CONTENT, success=True, message="Patient deleted successfully")