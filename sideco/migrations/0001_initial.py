# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cuil', models.CharField(max_length=12)),
                ('razon_social', models.TextField()),
                ('rubro', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='OfertaLaboral',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo_de_trabajo_solicitado', models.TextField()),
                ('empresa', models.ForeignKey(to='sideco.Empresa')),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('DNI', models.CharField(max_length=10)),
                ('tipo_de_trabajo', models.TextField()),
                ('fecha_de_nacimiento', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Sistema',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Desempleado',
            fields=[
                ('persona_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='sideco.Persona')),
            ],
            bases=('sideco.persona',),
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('persona_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='sideco.Persona')),
                ('empresa', models.ForeignKey(to='sideco.Empresa')),
            ],
            bases=('sideco.persona',),
        ),
    ]
