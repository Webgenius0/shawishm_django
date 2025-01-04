from django.urls import path
from . import views

urlpatterns = [
    path('patients/', views.PatientList.as_view(), name='patients_list'),
    path('patients/<int:pk>', views.PatientDetail.as_view(), name='patients_detail'),
]