from django.shortcuts import render, get_object_or_404 
import numpy as np
from PIL import Image
from Imagenes.models import *

from datetime import datetime
from NlpModel.model import *

def insert_caracteristicas(id_usuario, img):
    # Obtener el último ID de CaracteristicasImagene
    try:
        ultimo_id_caracteristica = CaracteristicasImagenes.objects.latest('id_caracteristica').id_caracteristica
        id_caracteristica = ultimo_id_caracteristica + 1
    except CaracteristicasImagenes.DoesNotExist:
        id_caracteristica = 1
    
    usuario_hijo = UsuariosHijos.objects.get(id_usuario_hijo=id_usuario)  # Obtén el usuario_hijo correcto basado en el id
    fecha_instante = datetime.now()  # Asigna la fecha y hora actual o la adecuada

    fecha_instante = datetime.now()  # Asigna la fecha y hora actual o la adecuada
    
    # Realizar análisis de la imagen
    caracteristicas_maximas = analizar_imagen(img)

    
    # Crea una instancia de CaracteristicasImagene
    caracteristicas = CaracteristicasImagenes(
        id_caracteristica=id_caracteristica,
        usuario_hijo=usuario_hijo,
        fecha_instante=fecha_instante,
        palabrotas=caracteristicas_maximas[0],
        sentido_neg=caracteristicas_maximas[1],
        sentido_neu=caracteristicas_maximas[2],
        sentido_pos=caracteristicas_maximas[3],
        emocion_others=caracteristicas_maximas[4],
        emocion_joy=caracteristicas_maximas[5],
        emocion_sadness=caracteristicas_maximas[6],
        emocion_anger=caracteristicas_maximas[7],
        emocion_surprise=caracteristicas_maximas[8],
        emocion_disgust=caracteristicas_maximas[9],
        emocion_fear=caracteristicas_maximas[10],
        odio_hateful=caracteristicas_maximas[11],
        odio_targeted=caracteristicas_maximas[12],
        odio_aggresive=caracteristicas_maximas[13],
        bullying=False
    )
    
    # Guarda la instancia en la base de datos
    caracteristicas.save()
    return caracteristicas

def insert_imagen(caracteristicas, img):
     # Obtener el último ID de Imagene
    try:
        ultimo_id_imagen = Imagenes.objects.latest('id_imagen').id_imagen
        id_imagen = ultimo_id_imagen + 1
    except Imagenes.DoesNotExist:
        id_imagen = 1

    # Crea una instancia de Imagene
    imagen = Imagenes(
        id_imagen=id_imagen,
        caracteristica=caracteristicas,
        ruta_imagen=f'D:/5to año/1er semestre\Taller\Proyecto_Final\media\{id_imagen}.png'
    )
    imagen.save()
    img.save(f'D:/5to año/1er semestre\Taller\Proyecto_Final\media\{id_imagen}.png')

    
def subir_imagen(request):
    if request.method == 'POST' and request.FILES['imagen']:
        id_usuario = int(request.POST['id'])
        

        imagen = request.FILES['imagen']
        img = Image.open(imagen)
        
        # Convertir la imagen a una matriz NumPy
        matriz_np = np.array(img)
        
        base_caracteristicas = insert_caracteristicas(id_usuario, matriz_np)

        insert_imagen(base_caracteristicas, img)
        

        

        return render(request, 'subir_imagen.html', {'mensaje': 'Características guardadas exitosamente.'})

    # filter = get_object_or_404(CaracteristicasImagenes, UsuariosHijos=1)
    print(CaracteristicasImagenes.objects.filter(usuario_hijo=1))
    
    return render(request, 'subir_imagen.html')
