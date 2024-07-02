from django.db import models

from django.db import models

class Comentario(models.Model):
    id = models.AutoField(primary_key=True)
    correo = models.EmailField()
    comentario = models.TextField()

    def __str__(self):
        return self.correo  
    
    class Meta:
        db_table = 'comentario' 


class Agencia(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=True)  # Cambio aplicado
    provincia = models.CharField(max_length=100, null=True)  # Cambio aplicado
    email = models.CharField(max_length=100, null=True)  # Cambio aplicado
    llamada = models.CharField(max_length=20, null=True)  # Cambio aplicado
    pagina_web = models.CharField(max_length=255, null=True)
    redes = models.CharField(max_length=255, null=True)
    imagen_url = models.CharField(max_length=255, null=True)
    es_publicidad = models.BooleanField(default=False)
    valoracion = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)

    class Meta:
        db_table = 'agencias'



class Celebracion(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=True)
    provincia = models.CharField(max_length=100, null=True)
    descripcion = models.CharField(max_length=255, null=True)
    horario = models.CharField(max_length=100, null=True)
    fechas = models.CharField(max_length=255, null=True, default='Desconocida')
    ubicacion = models.CharField(max_length=255, null=True)
    imagen_url = models.CharField(max_length=255, null=True)
    es_publicidad = models.BooleanField(default=False)
    valoracion = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)

    class Meta:
        db_table = 'celebraciones'


class Hotel(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=True)
    provincia = models.CharField(max_length=100, null=True)
    costo = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    habitaciones = models.IntegerField(null=True)
    bano = models.IntegerField(null=True)  # Considera cambiar a models.BooleanField si aplica
    garaje = models.BooleanField(null=True)  # models.BooleanField no permite null, considera cambiar a models.IntegerField si requiere null
    tamano = models.CharField(max_length=100, null=True)
    mensaje = models.CharField(max_length=255, null=True)
    llamada = models.CharField(max_length=20, null=True)
    ubicacion = models.CharField(max_length=255, null=True)
    redes = models.CharField(max_length=255, null=True)
    imagen_url = models.CharField(max_length=255, null=True)
    es_publicidad = models.BooleanField(default=False)  # Corregido para alinearse con MySQL
    valoracion = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)

    class Meta:
        db_table = 'hoteles'



class LugarTuristico(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=True)
    provincia = models.CharField(max_length=100, null=True)
    descripcion = models.CharField(max_length=255, null=True)
    horario = models.CharField(max_length=100, null=True)
    fecha_fundacion = models.CharField(max_length=255, null=True)
    ubicacion = models.CharField(max_length=255, null=True)
    imagen_url = models.CharField(max_length=255, null=True)
    es_publicidad = models.BooleanField(default=False)
    valoracion = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)

    class Meta:
        db_table = 'lugares_turisticos'



class Restaurante(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=True)
    provincia = models.CharField(max_length=100, null=True)
    dias = models.CharField(max_length=100, null=True)
    horario = models.CharField(max_length=100, null=True)
    sms = models.CharField(max_length=20, null=True)
    llamada = models.CharField(max_length=20, null=True)
    ubicacion = models.CharField(max_length=255, null=True)
    redes = models.CharField(max_length=255, null=True)
    imagen_url = models.CharField(max_length=255, null=True)
    es_publicidad = models.BooleanField(default=False)
    valoracion = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)

    class Meta:
        db_table = 'restaurantes'

