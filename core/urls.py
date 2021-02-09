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
    path('records', views.records, name="records"),
    path('recordNew', views.recordNew, name="recordNew"),
    # =====================
    path('nursing', views.nursing, name="nursing"),
    path('patientsn', views.patientsn, name="patientsn"),
    path('patientNew', views.patientNew, name="patientNew"),
    path('appointments', views.appointments, name="appointments"),
    path('appointmentNew', views.appointmentNew, name="appointmentNew"),
    # =====================
    path('pharmacist', views.pharmacist, name="pharmacist"),
    path('inventory', views.inventory, name="inventory"),
    path('inventoryNew', views.inventoryNew, name="inventoryNew"),
    path('inventoryDelete', views.inventoryDelete, name="inventoryDelete"),
]
