from django.urls import path, include
from .import views




urlpatterns = [
    #  path('',views.home,name='home'),
     path('account/', include('django.contrib.auth.urls')),
       path('dashboard', views.admin_dashboard_view,name='dashboard'),

    path('doctor', views.admin_doctor_view,name='doctor'),
    path('view-doctor', views.admin_view_doctor_view,name='view-doctor'),
    path('delete-doctor-from-hospital/<int:pk>', views.delete_doctor_from_hospital_view,name='delete-doctor-from-hospital'),
    path('update-doctor/<int:pk>', views.update_doctor_view,name='update-doctor'),
    path('add-doctor', views.admin_add_doctor_view,name='add-doctor'),
    path('approve-doctor', views.admin_approve_doctor_view,name='approve-doctor'),
    path('approve-doctor/<int:pk>', views.approve_doctor_view,name='approve-doctor'),
    path('reject-doctor/<int:pk>', views.reject_doctor_view,name='reject-doctor'),
    path('view-specialist',views.admin_view_doctor_specialisation_view,name='admin-view-specialist'),


    path('patient', views.admin_patient_view,name='patient'),
    path('view-patient', views.admin_view_patient_view,name='view-patient'),
    path('delete-patient-from-hospital/<int:pk>', views.delete_patient_from_hospital_view,name='delete-patient-from-hospital'),
    path('update-patient/<int:pk>', views.update_patient_view,name='update-patient'),
    path('add-patient', views.admin_add_patient_view,name='add-patient'),
    path('approve-patient', views.admin_approve_patient_view,name='approve-patient'),
    path('approve-patient/<int:pk>', views.approve_patient_view,name='approve-patient'),
    path('reject-patient/<int:pk>', views.reject_patient_view,name='reject-patient'),
    path('discharge-patient', views.admin_discharge_patient_view,name='discharge-patient'),
    path('discharge-patient/<int:pk>', views.discharge_patient_view,name='discharge-patient'),
  


    path('appointment', views.admin_appointment_view,name='appointment'),
    path('view-appointment', views.admin_view_appointment_view,name='view-appointment'),
    path('add-appointment', views.admin_add_appointment_view,name='add-appointment'),
    path('approve-appointment', views.admin_approve_appointment_view,name='approve-appointment'),
    path('approve-appointment/<int:pk>', views.approve_appointment_view,name='approve-appointment'),
    path('reject-appointment/<int:pk>', views.reject_appointment_view,name='reject-appointment'),
    
    
    
]