# Generated by Django 5.0.6 on 2024-05-26 20:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clase', '0002_alter_curso_nombre'),
        ('estudiante', '0002_remove_clase_precio_total_alter_estudiante_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='clase',
            name='profesor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='clase.profesor'),
        ),
    ]