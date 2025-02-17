from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Studies
from .serializers import StudiesSerializer , StudiesPOSTSerializer , MergepatientsSerializer , MergeStudiesSerializer

from patients.models import Patients
from referralPhysician.models import Referralphysician
from radiologyGroup.models import RadiologyGroup




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

        user = request.user

        try:
            studies = Studies.objects.select_related('pat_inc_id_det', 'ref_inc', 'radiology_group')

            if user.is_superuser or user.is_admin:
                serializer = StudiesSerializer(studies, many=True)
                return custom_response( status=status.HTTP_200_OK, success=True, message="Studies fetched successfully for admin or superadmin", data = serializer.data)
            elif user.is_ref_physician_user:
                filtered_studies = studies.filter(ref_inc__Ref_Phy_Name = user.U_fullname)
                serializer = StudiesSerializer(filtered_studies, many=True)
                return custom_response( status=status.HTTP_200_OK, success=True, message="Studies fetched successfully for Referral Physician", data = serializer.data)
            elif user.is_radiologist_user:
                filtered_studies = studies.filter(radiology_group__Rg_Name = user.U_fullname)
                serializer = StudiesSerializer(filtered_studies, many=True)
                return custom_response( status=status.HTTP_200_OK, success=True, message="Studies fetched successfully for Radiologist", data = serializer.data)
            else:
                return custom_response( status=status.HTTP_404_NOT_FOUND, success=False, message="User is not authorized to access the data")
        except Studies.DoesNotExist:
            return custom_response( status=status.HTTP_404_NOT_FOUND, success=False, message="Studies not found")
    
    def post(self, request):
        
        serializer = StudiesPOSTSerializer(data=request.data)
        patients_id = request.data.get('pat_inc_id_det' , None)
        physicians_id = request.data.get('ref_inc' , None)
        radiology_groups_id = request.data.get('radiology_group' , None)

        if serializer.is_valid():

            patient = None
            if patients_id:
                try:
                    patient = Patients.objects.get(pk=patients_id)
                except Patients.DoesNotExist:
                    return custom_response(status=status.HTTP_400_BAD_REQUEST, success=False, message="Invalid Patient ID")
                
            physician = None
            if physicians_id:
                try:
                    physician = Referralphysician.objects.get(pk=physicians_id)
                except Referralphysician.DoesNotExist:
                    return custom_response(status=status.HTTP_400_BAD_REQUEST, success=False, message="Invalid Physician ID")
        
            radiology_group = None
            if radiology_groups_id:
                try:
                    radiology_group = RadiologyGroup.objects.get(pk=radiology_groups_id)
                except RadiologyGroup.DoesNotExist:
                    return custom_response(status=status.HTTP_400_BAD_REQUEST, success=False, message="Invalid Radiology Group ID")
                
            serializer.save(pat_inc_id_det=patient, ref_inc=physician, radiology_group=radiology_group)
            return custom_response( status=status.HTTP_201_CREATED, success=True, message="Study created successfully", data = serializer.data)
        return custom_response( status=status.HTTP_400_BAD_REQUEST, success=False, message="Study not created", data = serializer.errors)
    

class StudiesDetail(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            study = Studies.objects.select_related('pat_inc_id_det', 'ref_inc', 'radiology_group').get(pk=pk)
            serializer = StudiesSerializer(study)
            return custom_response( status=status.HTTP_200_OK, success=True, message="Study fetched successfully", data = serializer.data)
        except Studies.DoesNotExist:
            return custom_response( status=status.HTTP_404_NOT_FOUND, success=False, message="Study not found")
        

    def patch(self, request, pk):
        try:
            study = Studies.objects.select_related('pat_inc_id_det', 'ref_inc', 'radiology_group').get(pk=pk)
        except Studies.DoesNotExist:
            return custom_response( status=status.HTTP_404_NOT_FOUND, success=False, message="Study not found")
        serializer = StudiesSerializer(study, data=request.data , partial=True)
        if serializer.is_valid():
            serializer.save()
            study.refresh_from_db()
            response = StudiesSerializer(study)

            return custom_response( status=status.HTTP_200_OK, success=True, message="Study updated successfully", data = response.data)
        return custom_response( status=status.HTTP_400_BAD_REQUEST, success=False, message="Study not updated", data = serializer.errors)
    

    def delete(self, request, pk):
        try:
            study = Studies.objects.select_related('pat_inc_id_det', 'ref_inc', 'radiology_group').get(pk=pk)
            study.delete()
            return custom_response( status=status.HTTP_204_NO_CONTENT, success=True, message="Study deleted successfully")
        except Studies.DoesNotExist:
            return custom_response( status=status.HTTP_404_NOT_FOUND, success=False, message="Study not found")


class AssignStudies(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        try:
            study = Studies.objects.select_related('pat_inc_id_det', 'ref_inc', 'radiology_group').get(pk=pk)
        except Studies.DoesNotExist:
            return custom_response( status=status.HTTP_404_NOT_FOUND, success=False, message="Study not found")
        serializer = StudiesSerializer(study, data=request.data , partial=True)
        if serializer.is_valid():
            serializer.save()
            study.refresh_from_db()
            response = StudiesSerializer(study)
            return custom_response( status=status.HTTP_200_OK, success=True, message="Studies assigned successfully", data = response.data)
        return custom_response( status=status.HTTP_400_BAD_REQUEST, success=False, message="Studies not assigned", data = serializer.errors)

class MergePatients(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        study = Studies.objects.select_related('pat_inc_id_det', 'ref_inc', 'radiology_group').get(pk=pk)
        serializer = MergepatientsSerializer(instance=study, data=request.data)
        
        
        if serializer.is_valid():
            serializer.save() 
            study_data_serializer = StudiesSerializer(study)
            return custom_response( status=status.HTTP_200_OK, success=True, message="Patients merged successfully", data = study_data_serializer.data)
        return custom_response( status=status.HTTP_400_BAD_REQUEST, success=False, message="Patients not merged", data = serializer.errors)
    

class MergeStudies(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        study = Studies.objects.select_related('pat_inc_id_det', 'ref_inc', 'radiology_group').get(pk=pk)
        serializer = MergeStudiesSerializer(instance=study, data=request.data , partial=True)   
        
        if serializer.is_valid():
            serializer.save() 
            study_data_serializer = StudiesSerializer(study)
            return custom_response( status=status.HTTP_200_OK, success=True, message="Studies merged successfully", data = study_data_serializer.data)
        return custom_response( status=status.HTTP_400_BAD_REQUEST, success=False, message="Studies not merged", data = serializer.errors)  