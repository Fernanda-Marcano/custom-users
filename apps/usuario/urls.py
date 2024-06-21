from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('register/', views.register_user, name='register'), 
    path('list/', views.list_user, name='list'), 
    path('edit/<int:id>/', views.edit_user, name='edit'),
    path('delete/<int:id>', views.delete_user, name='delete'),
    path('profile/', views.create_profile, name='profile')
]