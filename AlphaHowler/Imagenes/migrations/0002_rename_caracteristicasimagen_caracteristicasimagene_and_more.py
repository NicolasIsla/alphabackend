# Generated by Django 4.2.2 on 2023-06-10 02:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Imagenes', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CaracteristicasImagen',
            new_name='CaracteristicasImagene',
        ),
        migrations.RenameModel(
            old_name='Imagenes',
            new_name='Imagene',
        ),
        migrations.RenameModel(
            old_name='PadresHijos',
            new_name='PadresHijo',
        ),
        migrations.RenameModel(
            old_name='UsuariosHijos',
            new_name='UsuariosHijo',
        ),
        migrations.RenameModel(
            old_name='UsuariosPadres',
            new_name='UsuariosPadre',
        ),
    ]