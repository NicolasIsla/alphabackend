# Generated by Django 4.2.2 on 2023-06-10 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Imagenes', '0004_rename_caracteristicasimagene_caracteristicasimagenes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caracteristicasimagenes',
            name='palabrotas',
            field=models.IntegerField(default=0),
        ),
    ]
