from django.urls import path
from . import views

urlpatterns = [
    path('register-user/', views.register_user, name='register-user'), 
    path('list-user/', views.list_user, name='list-user'), 
    path('edit-user/<int:id>/', views.edit_user, name='edit-user'),
    path('delete-user/<int:id>/', views.delete_user, name='delete-user'),
    path('profile-detail/<int:id>/', views.detail_profile, name='detail-profile'),
    path('profile-edit/', views.edit_profile, name='edit-profile'),
] 

