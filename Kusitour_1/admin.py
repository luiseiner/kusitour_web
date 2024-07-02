from django.contrib import admin

# Importar los modelos
from .models import Agencia, Comentario, Celebracion, Hotel, LugarTuristico, Restaurante

admin.site.register(Agencia)
admin.site.register(Comentario)
admin.site.register(Celebracion)
admin.site.register(Hotel)
admin.site.register(LugarTuristico)
admin.site.register(Restaurante)
