from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('', views.landingpage, name='landingpage'),
    path('doctorclick', views.doctorclick),
    path('patientclick', views.patientclick),
    
    path('doctorsignup', views.doctor_signup,name='doctor/signup'),
    path('patientsignup', views.patient_signup_view),
    
    path('doctorlogin', LoginView.as_view(template_name='doctor/login.html')),
    path('patientlogin', LoginView.as_view(template_name='patient/patientlogin.html')),
    
    path('afterlogin', views.afterlogin,name='afterlogin'),
    path('logout', LogoutView.as_view(template_name='index.html'),name='logout'),
    
    path('doctor-dashboard', views.doctor_dashboard,name='doctor-dashboard'),
    path('search', views.search,name='search'),
    
    path('doctor-patient', views.doctor_patient,name='doctor-patient'),
    path('doctor-view-patient', views.doctor_view_patient,name='doctor-view-patient'),
    path('doctor-view-discharge-patient',views.doctor_view_discharge_patient,name='doctor-view-discharge-patient'),
    
    
    path('doctor-appointment', views.doctor_appointment,name='doctor-appointment'),
    path('doctor-view-appointment', views.doctor_view_appointment,name='doctor-view-appointment'),
    path('doctor-delete-appointment',views.doctor_delete_appointment,name='doctor-delete-appointment'),
    path('delete-appointment/<int:pk>', views.delete_appointment,name='delete-appointment'),


    path('patient-dashboard', views.patient_dashboard_view,name='patient-dashboard'),
    path('patient-appointment', views.patient_appointment_view,name='patient-appointment'),
    path('patient-book-appointment', views.patient_book_appointment_view,name='patient-book-appointment'),
    path('patient-view-appointment', views.patient_view_appointment_view,name='patient-view-appointment'),
    path('patient-view-doctor', views.patient_view_doctor_view,name='patient-view-doctor'),
    path('searchdoctor', views.search_doctor_view,name='searchdoctor'),
    path('patient-discharge', views.patient_discharge_view,name='patient-discharge'),
    
    
    
]
