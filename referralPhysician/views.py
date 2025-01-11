from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Referralphysician
from .serializers import ReferralPhysicianSerializer

# Create your views here.
def custom_response(status, success , message, data = None):
    return Response(
        {
            'status': status,
            'success': success,
            'message': message,
            'data': data
        }
    )


class ReferralphysicianList(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            referralphysicians = Referralphysician.objects.all()
            serializer = ReferralPhysicianSerializer(referralphysicians, many=True)
            return custom_response( status=status.HTTP_200_OK, success=True, message="Referral Physicians fetched successfully", data = serializer.data)
        except Referralphysician.DoesNotExist:
            return custom_response( status=status.HTTP_404_NOT_FOUND, success=False, message="Referral Physicians not found")

    def post(self, request):
        serializer = ReferralPhysicianSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return custom_response( status=status.HTTP_201_CREATED, success=True, message="Referral Physician created successfully", data = serializer.data)
        return custom_response( status=status.HTTP_400_BAD_REQUEST, success=False, message="Referral Physician not created", data = serializer.errors)
    
class ReferralphysicianDetail(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            referralphysician = Referralphysician.objects.get(pk=pk)
            serializer = ReferralPhysicianSerializer(referralphysician)
            return custom_response( status=status.HTTP_200_OK, success=True, message="Referral Physician fetched successfully", data = serializer.data)
        except Referralphysician.DoesNotExist:
            return  custom_response( status=status.HTTP_404_NOT_FOUND, success=False, message="Referral Physician not found")

    def put(self, request, pk):
        try:
            referralphysician = Referralphysician.objects.get(pk=pk)
            serializer = ReferralPhysicianSerializer(referralphysician, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return custom_response( status=status.HTTP_200_OK, success=True, message="Referral Physician updated successfully", data = serializer.data)
            return custom_response( status=status.HTTP_400_BAD_REQUEST, success=False, message="Referral Physician not updated", data = serializer.errors)
        except Referralphysician.DoesNotExist:
            return custom_response( status=status.HTTP_404_NOT_FOUND, success=False, message="Referral Physician not found")

        
    def delete(self, request, pk):
        try:
            referralphysician = Referralphysician.objects.get(pk=pk)
            referralphysician.delete()
            return custom_response( status=status.HTTP_204_NO_CONTENT, success=True, message="Referral Physician deleted successfully")
        except Referralphysician.DoesNotExist:
            return custom_response( status=status.HTTP_404_NOT_FOUND, success=False, message="Referral Physician not found")
