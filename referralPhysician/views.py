from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Referralphysician
from .serializers import ReferralPhysicianSerializer

# Create your views here.
class ReferralphysicianList(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            referralphysicians = Referralphysician.objects.all()
            serializer = ReferralPhysicianSerializer(referralphysicians, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Referralphysician.DoesNotExist:
            return Response({'error': 'Referral Physician not found'}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = ReferralPhysicianSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ReferralphysicianDetail(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            referralphysician = Referralphysician.objects.get(pk=pk)
            serializer = ReferralPhysicianSerializer(referralphysician)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Referralphysician.DoesNotExist:
            return Response({'error': 'Referral Physician not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            referralphysician = Referralphysician.objects.get(pk=pk)
            serializer = ReferralPhysicianSerializer(referralphysician, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Referralphysician.DoesNotExist:
            return Response({'error': 'Referral Physician not found'}, status=status.HTTP_404_NOT_FOUND)

        
    def delete(self, request, pk):
        try:
            referralphysician = Referralphysician.objects.get(pk=pk)
            referralphysician.delete()
            return Response({'success': 'Referral Physician deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Referralphysician.DoesNotExist:
            return Response({'error': 'Referral Physician not found'}, status=status.HTTP_404_NOT_FOUND)
