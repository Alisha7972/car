from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
path('', views.index, name='index'),
path('list/', views.members_list_partial, name='list_partial'),
path('create/', views.create_member, name='create'),
path('<int:pk>/json/', views.member_json, name='member_json'),
path('<int:pk>/update/', views.update_member, name='update'),
path('<int:pk>/delete/', views.delete_member, name='delete'),
]



# from django.urls import path
# from . import views

# urlpatterns = [
#     path('users/', views.index, name='members_index'),
#     path('users/create/', views.create_member, name='create_member'),
#     path('users/<int:pk>/update/', views.update_member, name='update_member'),
#     path('users/<int:pk>/delete/', views.delete_member, name='delete_member'),
#     path('users/<int:pk>/json/', views.member_json, name='member_json'),
# ]
