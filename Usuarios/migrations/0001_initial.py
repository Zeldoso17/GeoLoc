# Generated by Django 4.1 on 2022-08-11 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('nombre', models.CharField(max_length=70, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=70, verbose_name='Apellidos')),
                ('username', models.CharField(max_length=50, unique=True, verbose_name='Nombre de usuario')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Correo Electronico')),
                ('telefono', models.CharField(max_length=10, unique=True, verbose_name='Numero de telefono')),
                ('usuario_administrador', models.BooleanField(default=False)),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
            },
        ),
    ]