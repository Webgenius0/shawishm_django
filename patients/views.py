from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Patients
from .serializers import PatientsSerializer


# Create your views here.
class PatientList(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        patients = Patients.objects.all()
        serializer = PatientsSerializer(patients, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = PatientsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PatientDetail(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        patient = Patients.objects.get(pk=pk)
        serializer = PatientsSerializer(patient)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        patient = Patients.objects.get(pk=pk)
        serializer = PatientsSerializer(patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        patient = Patients.objects.get(pk=pk)
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)