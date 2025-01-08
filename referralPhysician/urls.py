from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReferralphysicianList.as_view(), name='referralphysician_list'),
    path('<uuid:pk>/', views.ReferralphysicianDetail.as_view(), name='referralphysician_detail'),
]