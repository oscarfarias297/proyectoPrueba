# Generated by Django 5.0.4 on 2024-05-06 03:02

import cliente.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True, verbose_name=cliente.models.Pais)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('apellido', models.CharField(max_length=80)),
                ('nacimiento', models.DateField(blank=True, null=True)),
                ('pais_origen', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cliente.pais')),
                ('provincia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cliente.provincia')),
            ],
        ),
    ]
