from django.urls import path
from . import views


urlpatterns = [
    path('', views.RadiologyGroupList.as_view(), name='radiologyGroup_list'),
    path('<uuid:pk>/', views.RadiologyGroupDetail.as_view(), name='radiologyGroup_detail'),
]
