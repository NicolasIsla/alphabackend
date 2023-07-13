from django.db import models

# Create your models here.

class UsuariosPadres(models.Model):
    id_usuario_padre = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo_electronico = models.EmailField()
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    

class UsuariosHijos(models.Model):
    id_usuario_hijo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    sexo_opciones = [
        ('F', 'Femenino'),
        ('M', 'Masculino')
            ]
    
    sexo = models.CharField(max_length=1, choices=sexo_opciones, default="F")

    planes_opciones = [
        ('P', 'Premium')
            ]
    plan = models.CharField(max_length=1, choices=planes_opciones, default="P")
    
    fecha_nacimiento = models.DateField()

    # Otros campos relevantes
    
    def __str__(self):
        # return f"{self.nombre} {self.apellido}"
        return f"{self.id_usuario_hijo}"


class PadresHijos(models.Model):
    usuario_padre = models.ForeignKey(UsuariosPadres, on_delete=models.CASCADE)
    usuario_hijo = models.ForeignKey(UsuariosHijos, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Relación: {self.usuario_padre} - {self.usuario_hijo}"


class CaracteristicasImagenes(models.Model):
    id_caracteristica = models.IntegerField(primary_key=True)
    usuario_hijo = models.ForeignKey(UsuariosHijos, on_delete=models.CASCADE)
    fecha_instante = models.DateTimeField()
    # caracteristicas
    palabrotas = models.IntegerField(default=0)
    sentido_neg = models.FloatField(default=0)
    sentido_neu= models.FloatField(default=0)
    sentido_pos = models.FloatField(default=0)
    emocion_others = models.FloatField(default=0)
    emocion_joy = models.FloatField(default=0)
    emocion_sadness = models.FloatField(default=0)
    emocion_anger = models.FloatField(default=0)
    emocion_surprise = models.FloatField(default=0)
    emocion_disgust = models.FloatField(default=0)
    emocion_fear = models.FloatField(default=0)
    odio_hateful = models.FloatField(default=0)
    odio_targeted = models.FloatField(default=0)
    odio_aggresive = models.FloatField(default=0)
    # resultados
    bullying = models.BooleanField(default=False)


    def __str__(self):
        return f"Caso: {self.id_caracteristica} - Niño: {self.usuario_hijo}"
    


class Imagenes(models.Model):
    id_imagen = models.IntegerField(primary_key=True)
    caracteristica = models.ForeignKey(CaracteristicasImagenes, on_delete=models.CASCADE)
    ruta_imagen = models.CharField(max_length=255)
    # Otros campos relevantes
    def __str__(self):
        return f"Imagen: {self.id_imagen} - Niño: {self.caracteristica.usuario_hijo}"
    
