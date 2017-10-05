# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-01 00:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Desocupado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DNI', models.CharField(max_length=10)),
                ('nombre', models.TextField()),
                ('apellido', models.TextField()),
                ('fecha_de_nacimiento', models.TextField()),
                ('profesion', models.TextField()),
                ('experiencia_laboral', models.TextField()),
                ('formacion', models.TextField()),
                ('habilidades', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuil', models.CharField(max_length=12)),
                ('razon_social', models.TextField()),
                ('rubro', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OfertaLaboral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_de_trabajo_solicitado', models.TextField()),
            ],
        ),
    ]