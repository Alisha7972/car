from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('models/', views.models, name='models'),
    path('blog/', views.blog, name='blog'),
    path('client_section', views.client_section, name='client_section'),

    path('', views.car_list, name="car_list"),
    path('add-car/', views.add_car, name="add_car"),
]
