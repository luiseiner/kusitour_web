from django import forms
from .models import Agencia, Celebracion, Hotel, LugarTuristico, Restaurante, Comentario

class AgenciaForm(forms.ModelForm):
    imagen_url = forms.ImageField(required=True)  # Especificar que el campo es una imagen

    class Meta:
        model = Agencia
        fields = ['nombre', 'provincia', 'email', 'llamada', 'pagina_web', 'redes', 'imagen_url', 'es_publicidad', 'valoracion']

    def __init__(self, *args, **kwargs):
        super(AgenciaForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['imagen_url'].required = False


class CelebracionForm(forms.ModelForm):
    imagen_url = forms.ImageField(required=True)  # Especificar que el campo es una imagen

    class Meta:
        model = Celebracion
        fields = ['nombre', 'provincia', 'descripcion', 'horario', 'fechas', 'ubicacion', 'imagen_url', 'es_publicidad', 'valoracion']

    def __init__(self, *args, **kwargs):
        super(CelebracionForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['imagen_url'].required = False


class HotelForm(forms.ModelForm):
    imagen_url = forms.ImageField(required=True)  # Especificar que el campo es una imagen

    class Meta:
        model = Hotel
        fields = ['nombre', 'provincia', 'costo', 'habitaciones', 'bano', 'garaje', 'tamano', 'mensaje', 'llamada', 'ubicacion', 'redes', 'imagen_url', 'es_publicidad', 'valoracion']

    def __init__(self, *args, **kwargs):
        super(HotelForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['imagen_url'].required = False


class LugarTuristicoForm(forms.ModelForm):
    imagen_url = forms.ImageField(required=True)  # Especificar que el campo es una imagen

    class Meta:
        model = LugarTuristico
        fields = ['nombre', 'provincia', 'descripcion', 'horario', 'fecha_fundacion', 'ubicacion', 'imagen_url', 'es_publicidad', 'valoracion']

    def __init__(self, *args, **kwargs):
        super(LugarTuristicoForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['imagen_url'].required = False


class RestauranteForm(forms.ModelForm):
    imagen_url = forms.ImageField(required=False)

    class Meta:
        model = Restaurante
        fields = ['nombre', 'provincia', 'dias', 'horario', 'sms', 'llamada', 'ubicacion', 'redes', 'imagen_url', 'es_publicidad', 'valoracion']

    def __init__(self, *args, **kwargs):
        super(RestauranteForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['imagen_url'].required = False


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['correo', 'comentario']