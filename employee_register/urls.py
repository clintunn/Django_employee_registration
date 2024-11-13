from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_form,name='employee_insert'), # for inseert operations
    path('<int:id>/', views.employee_form,name='employee_update'), # for update operation
    path('delete/<int:id>/', views.employee_delete,name='employee_delete'),
    path('lists/',views.employee_list,name='employee_list') # for retrieving and displaying all records
]


