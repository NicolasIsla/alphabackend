from django.contrib import admin
from Imagenes.models import *

# Register your models here.
admin.site.register(UsuariosHijos)
admin.site.register(UsuariosPadres)
admin.site.register(PadresHijos)
admin.site.register(CaracteristicasImagenes)
admin.site.register(Imagenes)

