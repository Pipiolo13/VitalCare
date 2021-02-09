from django.db import models
from django.contrib.auth.models import User as UserManager
from django.db.models.deletion import DO_NOTHING
#from django import forms
from django import forms
# Create your models here.
# Creamos una funcion que nos deveulva el titulo concatenado con la fecha


# def __str__(self):
#    return self.title + " " + str(self.created)


class Question(models.Model):  # Preguntas de seguridad
    quest = models.TextField(verbose_name="Pregunta de seguridad")
# creamos clase meta para el nombre a mostrar, y el orden en que se muestran

    class Meta:
        verbose_name = "Pregunta"
        verbose_name_plural = "Preguntas"
        # ordering = ["created"]

    def __str__(self):
        return self.quest


# usuarios hereda el id nombre apellido correo y grupos de User del sistema de django
class Userdata(models.Model):
    user = models.OneToOneField(UserManager, on_delete=models.CASCADE)
    gender = models.CharField(verbose_name="Genero", max_length=50)
    address = models.TextField(verbose_name="Direccion")
    dni = models.CharField(verbose_name="Identificacion", max_length=255)
    phone = models.CharField(verbose_name="Telefono", max_length=20)
    image = models.ImageField(verbose_name="Imagen", upload_to="bdd")
    created = models.DateTimeField(
        verbose_name="Fecha de creacion", auto_now_add=True)
    updated = models.DateTimeField(
        verbose_name="Fecha de actualizacion", auto_now=True)
    active = models.BooleanField(default=True)
    usertipe = models.CharField(verbose_name="Tipo de usuario", max_length=255)
    question = models.ForeignKey(
        Question, verbose_name="Seguridad", on_delete=DO_NOTHING)
    answer = models.CharField(
        verbose_name="Respuesta de seguridad", max_length=255)

# creamos clase meta para el nombre a mostrar, y el orden en que se muestran
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        ordering = ["created"]

    def __str__(self):
        return self.name


class Medic(models.Model):
    iduser = models.ForeignKey(
        UserManager, verbose_name="Usuario id", on_delete=DO_NOTHING)
    updated = models.DateTimeField(
        verbose_name="Fecha de actualizacion", auto_now=True)
    active = models.BooleanField(default=True)
    maxturn = models.IntegerField(verbose_name="Turnos maximos")
    entrytime = models.TimeField(verbose_name="Hora de entrada")
    departuretime = models.TimeField(verbose_name="Hora de salida")

    class Meta:
        verbose_name = "Medico"
        verbose_name_plural = "Medicos"
        ordering = ["updated"]

    def __str__(self):
        return self.iduser


class Specialty (models.Model):
    name = models.CharField(verbose_name="Nombre", max_length=255)

    class Meta:
        verbose_name = "Especialidad"
        verbose_name_plural = "Especialidades"
        ordering = ["name"]

    def __str__(self):
        return self.name


class MedicSpecialty (models.Model):
    medicid = models.ForeignKey(
        Medic, verbose_name="Medico id", on_delete=DO_NOTHING)
    specialtyid = models.ForeignKey(
        Specialty, verbose_name="Especialidad id", on_delete=DO_NOTHING)

    class Meta:
        verbose_name = "Medico especialidad"
        verbose_name_plural = "Medico especialidad"

    def __str__(self):
        return self.specialtyid


class Supplier (models.Model):  # tabla proveedor
    name = models.CharField(verbose_name="Nombre", max_length=255)
    company = models.CharField(verbose_name="Compañia", max_length=255)
    email = models.EmailField(verbose_name="Correo")
    phone = models.CharField(verbose_name="Telefono", max_length=20)

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Category (models.Model):  # tabla categoria de productos medicos
    name = models.CharField(verbose_name="Nombre", max_length=255)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Product (models.Model):  # tabla productos
    categoryid = models.ForeignKey(
        Category, verbose_name="Categoria id", on_delete=DO_NOTHING)
    supplierid = models.ForeignKey(
        Supplier, verbose_name="Proveedor id", on_delete=DO_NOTHING)
    name = models.CharField(verbose_name="Nombre", max_length=255)
    cost = models.DecimalField(
        verbose_name="Costo", max_digits=5, decimal_places=2)
    packagevalue = models.DecimalField(
        verbose_name="Valor paquete", max_digits=5, decimal_places=2)
    unitvalue = models.DecimalField(
        verbose_name="Valor unitario", max_digits=5, decimal_places=2)
    stocks = models.IntegerField(verbose_name="Stock")
    duedate = models.DateField(verbose_name="Fecha de vencimiento")
    updated = models.DateTimeField(
        verbose_name="Fecha de actualizacion", auto_now=True)
    usermodified = models.ForeignKey(
        UserManager, verbose_name="Ultimo Usuario modificador", on_delete=DO_NOTHING)
    code = models.CharField(verbose_name="Codigo", max_length=255)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Patient (models.Model):  # tabla paciente con los datos basicos del paciente
    name = models.CharField(verbose_name="Nombre", max_length=255)
    lastname = models.CharField(verbose_name="Apellido", max_length=255)
    email = models.EmailField(verbose_name="Correo")
    gender = models.CharField(verbose_name="Genero", max_length=50)
    address = models.TextField(verbose_name="Direccion")
    dni = models.CharField(verbose_name="Identificacion", max_length=255)
    phone = models.CharField(verbose_name="Telefono", max_length=20)
    created = models.DateTimeField(
        verbose_name="Fecha de creacion", auto_now_add=True)
    updated = models.DateTimeField(
        verbose_name="Fecha de actualizacion", auto_now=True)
    usermodified = models.ForeignKey(
        UserManager, verbose_name="Ultimo Usuario modificador", on_delete=DO_NOTHING)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Record(models.Model):
    patientid = models.ForeignKey(
        Patient, verbose_name="Paciente id", on_delete=DO_NOTHING)
    created = models.DateTimeField(
        verbose_name="Fecha de creacion", auto_now_add=True)
    feeding = models.TextField(verbose_name="Alimentacion")
    diuresis = models.TextField(verbose_name="Diuresis")
    catharsis = models.TextField(verbose_name="Catarsis")
    diseases = models.TextField(verbose_name="Enfermedades")
    hereditary = models.TextField(verbose_name="Enfermedades heredofamiliares")
    menstrual = models.TextField(verbose_name="Menstruales")
    sexual = models.TextField(verbose_name="Sexuales")
    menarca = models.TextField(verbose_name="Menarca")
    mac = models.TextField(verbose_name="Mac")
    fun = models.TextField(verbose_name="Fun")
    menopause = models.TextField(verbose_name="Menopausia")
    papsmear = models.TextField(verbose_name="Papanicolao")
    mammography = models.TextField(verbose_name="Mamografia")
    feats = models.TextField(verbose_name="Gestas")
    deliveries = models.TextField(verbose_name="Partos")
    abortions = models.TextField(verbose_name="Abortos")
    caesarean = models.TextField(verbose_name="Cesareas")
    others = models.TextField(verbose_name="Otros")

    class Meta:
        verbose_name = "Antecedente"
        verbose_name_plural = "Antecedentes"
        ordering = ["created"]

    def __str__(self):
        return self.patientid


class Schedule(models.Model):
    medicid = models.ForeignKey(
        Medic, verbose_name="Medico id", on_delete=DO_NOTHING)
    patientid = models.ForeignKey(
        Patient, verbose_name="Paciente id", on_delete=DO_NOTHING)
    reason = models.TextField(verbose_name="Motivo")
    symptoms = models.TextField(verbose_name="Sintomas")
    medication = models.TextField(verbose_name="Medicacion")
    created = models.DateTimeField(
        verbose_name="Fecha de creacion", auto_now_add=True)
    dateappointment = models.DateTimeField(
        verbose_name="Fecha de la cita")
    usermodified = models.ForeignKey(
        UserManager, verbose_name="Ultimo Usuario modificador", on_delete=DO_NOTHING)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Agenda"
        verbose_name_plural = "Agenda"
        ordering = ["active"]

    def __str__(self):
        return self.name


class Examination(models.Model):
    observations = models.TextField(verbose_name="Observaciones")
    image = models.ImageField(verbose_name="Imagen", upload_to="bdd")

    class Meta:
        verbose_name = "Examen"
        verbose_name_plural = "Examenes"

    def __str__(self):
        return self.name


class Consultation(models.Model):
    scheduleid = models.ForeignKey(
        Schedule, verbose_name="Agenda di", on_delete=DO_NOTHING)
    dateattention = models.DateTimeField(
        verbose_name="Fecha de atencion", auto_now_add=True)
    height = models.DecimalField(
        verbose_name="Altura", max_digits=5, decimal_places=2)
    weight = models.DecimalField(
        verbose_name="Peso", max_digits=5, decimal_places=2)
    imc = models.DecimalField(
        verbose_name="Indice de masa corporal", blank=True, max_digits=5, decimal_places=2)
    exploration = models.TextField(verbose_name="Exploracion")
    examinationid = models.ForeignKey(
        Examination, verbose_name="Examen id", on_delete=DO_NOTHING)
    sickness = models.TextField(verbose_name="Enfermedad actual")
    temperature = models.DecimalField(
        verbose_name="Temperatura", max_digits=5, decimal_places=2)
    heartfrequency = models.DecimalField(
        verbose_name="Frecuencia cardiaca", max_digits=5, decimal_places=2)
    breathingfrequency = models.DecimalField(
        verbose_name="Frecuencia respiratoria", max_digits=5, decimal_places=2)
    diagnosis = models.TextField(verbose_name="Diagnostico")
    medication = models.TextField(verbose_name="Medicacion")
    recommendations = models.TextField(verbose_name="Recomendaciones")

    class Meta:
        verbose_name = "Consulta"
        verbose_name_plural = "Consultas"

    def __str__(self):
        return self.name
