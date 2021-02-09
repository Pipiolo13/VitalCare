from django.contrib.auth import login as do_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import logout as do_logout
from django.forms import ModelForm
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .models import Userdata, Product, Patient, Schedule, Record
from django.contrib.auth.models import User, Group
from .forms import ProductForm, PatientForm, RecordForm, ScheduleForm,Consultation,ConsultationForm

# Create your views here.


def index(request):
    if request.user.is_authenticated:
        # Finalizamos la sesión
        do_logout(request)
    return render(request, "core/index.html")


def login(request):
    return render(request, "core/login.html")


def home(request):
    # En otro caso redireccionamos al login
    return redirect('/login')


def base(request):
    return render(request, "core/base.html")


def register(request):
    return render(request, "core/register.html")


# ...


def login(request):
    # creamos una lista para todos los grupos
    medic_group = Group.objects.get(name="medic").user_set.all()
    nursing_group = Group.objects.get(name="nursing").user_set.all()
    pharmacist_group = Group.objects.get(name="pharmacist").user_set.all()
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()

    """ esta variable en caso de usar el Login form de forms.py
    Si se activa esta comentar el form de arriba
    Tambien cambiar el <form> en login.py, y mover los tags {% commit %} al otro form con estilos
    e importar en .forms el LoginForm,
    form = LoginForm() """
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:

                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada

                # Si estamos identificados devolvemos la portada
                if request.user.is_authenticated:
                    if request.user in medic_group:
                        return redirect("medic")
                    if request.user in nursing_group:
                        return redirect("nursing")
                    if request.user in pharmacist_group:
                        return redirect("pharmacist")
                # return redirect('home/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "core/login.html", {'form': form})


# Seccion del farmaceuta
# =============================================================


# principal
def pharmacist(request):
    return render(request, "core/pharmacist/pharmacist.html")


# pagina de productos
def inventory(request):
    # almacenamos todos los datos de Productos en la variable
    invs = Product.objects.all()
    return render(request, "core/pharmacist/inventory.html", {"invs": invs})


# agregar un nuevo producto
def inventoryNew(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(data=request.POST)
        if form.is_valid():
            form.usermodified = request.user
            form.save()
            return redirect('inventory')
    return render(request, 'core/pharmacist/add-inventory.html', {'form': form})


# eliminar un producto del inventario de productos
# recivimos la id desde la lista de productos
def inventoryDelete(request, pk):
    # en inventory.html en el boton eliminar envio tambien el id, ese id lo recivo aqui y elimino ese registro por medio de ese id
    # almacenamos en una variable el producto que tenga ese id
    inv = get_object_or_404(Product, pk=pk,)
    if request.method == "POST":
        # eliminamos ese producto
        inv.delete()
        # redirect llamando al name de la url.py para volver a la lista de productos
        return redirect('inventory')
# ===================================================================


# Seccion de Doctores
# =============================================================
def medic(request):
    return render(request, "core/medic/medic.html")

# Pagina de agenda donde el doctor ve las citas que tiene para el dia


def schedule(request):
    citas = Schedule.objects.all()
    return render(request, "core/medic/schedule.html", {"citas": citas})

    # Entramos a una nueva consulta desde la agenda de citas con el id de la cita
def consultationNew(request, pk):
    cita = get_object_or_404(Patient, pk=pk)
    form = ConsultationForm()
    if request.method == "POST":
        form = ConsultationForm(request.POST, instance=cita)
        if form.is_valid():
            form.save()
            Schedule.objects.filter(id=pk).update(active=False)
            return redirect("patientsm")
    return render(request, "core/medic/add-consultation.html", {"form": form, 'pk': pk})


# primero Entra a los pacientes
def patientsm(request):
    pats = Patient.objects.all()
    return render(request, "core/medic/patients-m.html", {"pats": pats})


# para ver las consultas de un paciente se pide el id del mismo
def records(request, pk):
    recs = get_object_or_404(Record, pk=pk)
    return render(request, "core/medic/records.html", {'recs': recs})


# registramos la consulta del paciente con el id
def recordNew(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    form = RecordForm()
    if request.method == "POST":
        form = RecordForm(request.POST, instance=patient)
        if form.is_valid():
            form.usermodified = request.user
            form.save()
            return redirect('records')
    return render(request, "core/medic/add-record.html", {'form': form, 'pk': pk})
# =====================================================================


# Seccion de Enfermeros
# # ===============================================================
def nursing(request):
    return render(request, "core/nursing/nursing.html")


def patientsn(request):
    pats = Patient.objects.all()
    return render(request, "core/nursing/patients-n.html", {"pats": pats})


def patientNew(request):
    form = PatientForm()
    if request.method == "POST":
        form = PatientForm(data=request.POST)
        if form.is_valid():
            form.usermodified = request.user
            form.save()
            return redirect('patients-m')
    return render(request, 'core/nursing/add-patient.html', {'form': form})


# Enfermero tiene una lista de todas las citas
def appointments(request):
    # Para eso se crea una variable con todos los datos de la tabla Agenda "schedule" en ingles
    citas = Schedule.objects.all()
    return render(request, "core/nursing/appointments.html", {"citas": citas})


def appointmentNew(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    form = ScheduleForm()
    if request.method == "POST":
        form = ScheduleForm(request.POST, instance=patient)
        if form.is_valid():
            form.usermodified = request.user
            form.save()
            return render("appointments")
    return render(request, "core/nursing/add-appointment.html", {"form": form, 'pk': pk})

# ================================================================


""" 
#Sin implementar, se registra un usuario desde la pagina Admin
def register(request):
    # Creamos el formulario de autenticación vacío
    form = UserCreationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = UserCreationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():

            # Creamos la nueva cuenta de usuario
            user = form.save()

            # Si el usuario se crea correctamente
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "core/register.html", {'form': form})
"""
