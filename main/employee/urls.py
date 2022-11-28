from django.urls import path
from .import views

urlpatterns = [
    path('', views.employees_list,name='employees_list' ),
    path('create/', views.create_employee,name='create_employee' ),
    path('edit/<int:pk>', views.edit_employee,name='edit_employee' ),
    path('delete/<int:pk>', views.delete_employee,name='delete_employee' ), 
]