from django.contrib.auth.forms import AuthenticationForm
from .models import Supplier, Product, Patient, Record, Category, Schedule, Medic, MedicSpecialty, Specialty
from django import forms


""" class LoginForm(forms.ModelForm):
    # en caso de intentar usar el modelo de esta clase,
    # debe modificarse views.py en Login tal como se dice y modificar login.html
    class Meta:
        model = AuthenticationForm
        fields = "__all__" """


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = "__all__"


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['categoryid'].queryset = Category.objects.none()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['supplierid'].queryset = Supplier.objects.none()


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = "__all__"


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['patientid'].queryset = Patient.objects.none()


class MedicForm(forms.ModelForm):
    class Meta:
        model = Medic
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['patientid'].queryset = Patient.objects.none()


class MedicSpecialtyForm(forms.ModelForm):
    class Meta:
        model = MedicSpecialty
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['specialtyid'].queryset = Specialty.objects.none()


class SpecialtyForm(forms.ModelForm):
    class Meta:
        model = Specialty
        fields = "__all__"


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['medicid'].queryset = Medic.objects.none()
