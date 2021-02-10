# Generated by Django 2.2.7 on 2021-02-09 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_category_consultation_examination_medic_medicspecialty_patient_product_record_schedule_specialty_sup'),
    ]

    operations = [
        migrations.RenameField(
            model_name='consultation',
            old_name='diagnosis',
            new_name='diagnostic',
        ),
        migrations.RemoveField(
            model_name='consultation',
            name='scheduleid',
        ),
        migrations.AddField(
            model_name='consultation',
            name='patientid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.Patient', verbose_name='PacienteId'),
            preserve_default=False,
        ),
    ]