from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('home', views.home, name="home"),
    # =====================
    path('medic', views.medic, name="medic"),
    path('schedule', views.schedule, name="schedule"),
    path('patientsm', views.patientsm, name="patientsm"),
    path('records/<int:pk>', views.records, name="records"),
    path('recordNew/<int:pk>', views.recordNew, name="recordNew"),
    path('consultationNew/<int:pk>', views.consultationNew, name="consultationNew"),
    # =====================
    path('nursing', views.nursing, name="nursing"),
    path('patientsn', views.patientsn, name="patientsn"),
    path('patientNew', views.patientNew, name="patientNew"),
    path('appointments', views.appointments, name="appointments"),
    path('appointmentNew/<int:pk>', views.appointmentNew, name="appointmentNew"),
    # =====================
    path('pharmacist', views.pharmacist, name="pharmacist"),
    path('inventory', views.inventory, name="inventory"),
    path('inventoryNew', views.inventoryNew, name="inventoryNew"),
    path('inventoryDelete/<int:pk>', views.inventoryDelete, name="inventoryDelete"),
]
