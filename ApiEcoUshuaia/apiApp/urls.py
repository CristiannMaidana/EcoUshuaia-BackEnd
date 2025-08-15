from django.urls import path
from apiApp import views

urlpatterns = [
    path('residuos/', views.residuos_list),
    path('residuos/<int:pk>/', views.residuo_detail),
]