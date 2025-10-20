from django.urls import path
from . import views

urlpatterns = [
    path('', views.Ajax, name='ajax_home'),
]