from django.urls import path
from . import car_views as views

urlpatterns = [
    path('models/', views.models, name='models'),
    path('models/add/', views.car_add, name='car_add'),
    path('models/edit/<int:car_id>/', views.car_edit, name='car_edit'),
    path('models/delete/<int:car_id>/', views.car_delete, name='car_delete'),
]
