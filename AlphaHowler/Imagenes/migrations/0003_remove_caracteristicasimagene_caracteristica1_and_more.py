# Generated by Django 4.2.2 on 2023-06-10 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Imagenes', '0002_rename_caracteristicasimagen_caracteristicasimagene_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='caracteristicasimagene',
            name='caracteristica1',
        ),
        migrations.RemoveField(
            model_name='caracteristicasimagene',
            name='caracteristica2',
        ),
        migrations.AddField(
            model_name='caracteristicasimagene',
            name='bullying',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='caracteristicasimagene',
            name='emocion_anger',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='caracteristicasimagene',
            name='emocion_disgust',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='caracteristicasimagene',
            name='emocion_fear',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='caracteristicasimagene',
            name='emocion_joy',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='caracteristicasimagene',
            name='emocion_others',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='caracteristicasimagene',
            name='emocion_sadness',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='caracteristicasimagene',
            name='emocion_surprise',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='caracteristicasimagene',
            name='odio_aggresive',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='caracteristicasimagene',
            name='odio_hateful',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='caracteristicasimagene',
            name='odio_targeted',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='caracteristicasimagene',
            name='palabrotas',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='caracteristicasimagene',
            name='sentido_neg',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='caracteristicasimagene',
            name='sentido_neu',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='caracteristicasimagene',
            name='sentido_pos',
            field=models.FloatField(default=0),
        ),
    ]
