# Generated by Django 4.1 on 2022-12-07 02:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0002_usuarios_empresa'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuarios',
            old_name='empresa',
            new_name='isEmpresa',
        ),
    ]
