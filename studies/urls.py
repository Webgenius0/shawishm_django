from django.urls import path
from . import views

urlpatterns = [
    path('', views.StudiesList.as_view(), name='studies_list'),
    path('<int:pk>/', views.StudiesDetail.as_view(), name='studies_detail'),
    path('<int:pk>/mergepatients/', views.MergePatients.as_view(), name='studies_mergepatients'),

]