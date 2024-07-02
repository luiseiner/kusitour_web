from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Agencia, Celebracion, Hotel, LugarTuristico, Restaurante, Comentario
from .forms import AgenciaForm, CelebracionForm, HotelForm, LugarTuristicoForm, RestauranteForm, ComentarioForm
import boto3
import logging
from django.conf import settings
import os

# Configuración de logging
logger = logging.getLogger(__name__)

def index(request):
    template_path = os.path.join(settings.BASE_DIR, 'Kusitour_1', 'templates', 'index.html')
    print(f"Path to index.html: {template_path}")
    print("Exists:", os.path.exists(template_path))
    return render(request, 'index.html')

def somos(request):
    return render(request, 'somos.html')

def ingresar_comentario(request):
    return render(request, 'pregunta.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('listar_agencias')
        else:
            return render(request, 'login.html', {'error': 'Nombre de usuario o contraseña incorrectos'})
    else:
        return render(request, 'login.html')

@login_required
def listar_agencias(request):
    agencias = Agencia.objects.all()
    form = AgenciaForm()
    return render(request, 'listar_agencias.html', {'agencias': agencias, 'form': form})

@login_required
def agregar_agencia(request):
    if request.method == "POST":
        form = AgenciaForm(request.POST, request.FILES)
        if form.is_valid():
            agencia = form.save(commit=False)
            if 'imagen_url' in request.FILES:
                file = request.FILES['imagen_url']
                file_url = upload_to_s3(file, 'agencias')
                if file_url:
                    agencia.imagen_url = file_url
                else:
                    logger.error("No se pudo subir el archivo a S3.")
            agencia.save()
            return redirect('listar_agencias')
        else:
            logger.error("Errores en el formulario: %s", form.errors)
    else:
        form = AgenciaForm()
    return render(request, 'listar_agencias.html', {'form': form, 'agencias': Agencia.objects.all()})

@login_required
def editar_agencia(request, id):
    agencia = get_object_or_404(Agencia, pk=id)
    imagen_actual = agencia.imagen_url  # Guardar la URL de la imagen actual
    if request.method == "POST":
        form = AgenciaForm(request.POST, request.FILES, instance=agencia)
        
        # Log the data received
        logger.info(f"Datos recibidos para la edición: {request.POST}")
        logger.info(f"Archivos recibidos para la edición: {request.FILES}")
        
        if form.is_valid():
            logger.info("El formulario es válido.")
            agencia = form.save(commit=False)
            if 'imagen_url' in request.FILES:
                file = request.FILES['imagen_url']
                file_url = upload_to_s3(file, 'agencias')
                agencia.imagen_url = file_url
            else:
                agencia.imagen_url = imagen_actual  # Mantener la imagen actual si no se sube una nueva
            agencia.save()
            return redirect('listar_agencias')
        else:
            logger.error(f"Errores de validación del formulario: {form.errors}")
    return redirect('listar_agencias')

@login_required
def eliminar_agencia(request, id):
    agencia = get_object_or_404(Agencia, pk=id)
    agencia.delete()
    return redirect('listar_agencias')

@login_required
def listar_celebraciones(request):
    celebraciones = Celebracion.objects.all()
    form = CelebracionForm()
    return render(request, 'listar_celebraciones.html', {'celebraciones': celebraciones, 'form': form})

@login_required
def agregar_celebracion(request):
    if request.method == "POST":
        form = CelebracionForm(request.POST, request.FILES)
        if form.is_valid():
            celebracion = form.save(commit=False)
            if 'imagen_url' in request.FILES:
                file = request.FILES['imagen_url']
                file_url = upload_to_s3(file, 'celebraciones')
                if file_url:
                    celebracion.imagen_url = file_url
                else:
                    logger.error("No se pudo subir el archivo a S3.")
            celebracion.save()
            return redirect('listar_celebraciones')
        else:
            logger.error("Errores en el formulario: %s", form.errors)
    else:
        form = CelebracionForm()
    return render(request, 'listar_celebraciones.html', {'form': form, 'celebraciones': Celebracion.objects.all()})

@login_required
def editar_celebracion(request, pk):
    celebracion = get_object_or_404(Celebracion, pk=pk)
    if request.method == "POST":
        form = CelebracionForm(request.POST, request.FILES, instance=celebracion)
        if form.is_valid():
            celebracion = form.save(commit=False)
            if 'imagen_url' in request.FILES:
                file = request.FILES['imagen_url']
                file_url = upload_to_s3(file, 'celebraciones')
                if file_url:
                    celebracion.imagen_url = file_url
            celebracion.save()
            return redirect('listar_celebraciones')
        else:
            return render(request, 'editar_celebracion.html', {'form': form})
    else:
        form = CelebracionForm(instance=celebracion)
        return render(request, 'editar_celebracion.html', {'form': form})

@login_required
def eliminar_celebracion(request, id):
    celebracion = get_object_or_404(Celebracion, pk=id)
    celebracion.delete()
    return redirect('listar_celebraciones')

@login_required
def listar_hoteles(request):
    hoteles = Hotel.objects.all()
    form = HotelForm()
    return render(request, 'listar_hoteles.html', {'hoteles': hoteles, 'form': form})

@login_required
def agregar_hotel(request):
    if request.method == "POST":
        form = HotelForm(request.POST, request.FILES)
        if form.is_valid():
            hotel = form.save(commit=False)
            if 'imagen_url' in request.FILES:
                file = request.FILES['imagen_url']
                file_url = upload_to_s3(file, 'hoteles')
                if file_url:
                    hotel.imagen_url = file_url
                else:
                    logger.error("No se pudo subir el archivo a S3.")
            hotel.save()
            return redirect('listar_hoteles')
        else:
            logger.error("Errores en el formulario: %s", form.errors)
    else:
        form = HotelForm()
    return render(request, 'listar_hoteles.html', {'form': form, 'hoteles': Hotel.objects.all()})


@login_required
def editar_hotel(request, pk):
    hotel = get_object_or_404(Hotel, pk=pk)
    imagen_actual = hotel.imagen_url  # Guardar la URL de la imagen actual
    if request.method == "POST":
        form = HotelForm(request.POST, request.FILES, instance=hotel)
        
        # Log the data received
        logger.info(f"Datos recibidos para la edición: {request.POST}")
        logger.info(f"Archivos recibidos para la edición: {request.FILES}")
        
        if form.is_valid():
            logger.info("El formulario es válido.")
            hotel = form.save(commit=False)
            if 'imagen_url' in request.FILES:
                file = request.FILES['imagen_url']
                file_url = upload_to_s3(file, 'hoteles')
                if file_url:
                    hotel.imagen_url = file_url
            hotel.save()
            return redirect('listar_hoteles')
        else:
            logger.error(f"Errores de validación del formulario: {form.errors}")
    return redirect('listar_hoteles')

@login_required
def eliminar_hotel(request, id):
    hotel = get_object_or_404(Hotel, pk=id)
    hotel.delete()
    return redirect('listar_hoteles')


def upload_to_s3(file, folder='default_folder'):
    s3 = boto3.client('s3',
                      aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                      aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
                      region_name=settings.AWS_S3_REGION_NAME)
    
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME
    file_key = f'{folder}/{file.name}'
    
    try:
        s3.upload_fileobj(file, bucket_name, file_key, ExtraArgs={'ACL': 'public-read'})
        file_url = f'https://{bucket_name}.s3.{settings.AWS_S3_REGION_NAME}.amazonaws.com/{file_key}'
        return file_url
    except Exception as e:
        logger.error(f"Error subiendo archivo a S3: {e}")
        return None


@login_required
def listar_lugares_turisticos(request):
    lugares = LugarTuristico.objects.all()
    form = LugarTuristicoForm()
    return render(request, 'listar_lugares_turisticos.html', {'lugares': lugares, 'form': form})

@login_required
def agregar_lugar_turistico(request):
    if request.method == "POST":
        form = LugarTuristicoForm(request.POST, request.FILES)
        if form.is_valid():
            lugar = form.save(commit=False)
            if 'imagen_url' in request.FILES:
                file = request.FILES['imagen_url']
                file_url = upload_to_s3(file, 'lugares_turisticos')
                if file_url:
                    lugar.imagen_url = file_url
                else:
                    logger.error("No se pudo subir el archivo a S3.")
            lugar.save()
            return redirect('listar_lugares_turisticos')
        else:
            logger.error("Errores en el formulario: %s", form.errors)
    else:
        form = LugarTuristicoForm()
    return render(request, 'listar_lugares_turisticos.html', {'form': form, 'lugares': LugarTuristico.objects.all()})


@login_required
def editar_lugar_turistico(request, pk):
    lugar = get_object_or_404(LugarTuristico, pk=pk)
    imagen_actual = lugar.imagen_url  # Guardar la URL de la imagen actual
    if request.method == "POST":
        form = LugarTuristicoForm(request.POST, request.FILES, instance=lugar)
        
        # Log the data received
        logger.info(f"Datos recibidos para la edición: {request.POST}")
        logger.info(f"Archivos recibidos para la edición: {request.FILES}")
        
        if form.is_valid():
            logger.info("El formulario es válido.")
            lugar = form.save(commit=False)
            if 'imagen_url' in request.FILES:
                file = request.FILES['imagen_url']
                file_url = upload_to_s3(file, 'lugares_turisticos')
                lugar.imagen_url = file_url
                if file_url:
                    lugar.imagen_url = file_url
            lugar.save()
            return redirect('listar_lugares_turisticos')
        else:
            logger.error(f"Errores de validación del formulario: {form.errors}")
    return redirect('listar_lugares_turisticos')

@login_required
def eliminar_lugar_turistico(request, id):
    lugar = get_object_or_404(LugarTuristico, pk=id)
    lugar.delete()
    return redirect('listar_lugares_turisticos')

@login_required
def listar_restaurantes(request):
    restaurantes = Restaurante.objects.all()
    form = RestauranteForm()
    return render(request, 'listar_restaurantes.html', {'restaurantes': restaurantes, 'form': form})

@login_required
def agregar_restaurante(request):
    if request.method == "POST":
        form = RestauranteForm(request.POST, request.FILES)
        if form.is_valid():
            restaurante = form.save(commit=False)
            if 'imagen_url' in request.FILES:
                file = request.FILES['imagen_url']
                file_url = upload_to_s3(file, 'restaurantes')
                if file_url:
                    restaurante.imagen_url = file_url
                else:
                    logger.error("No se pudo subir el archivo a S3.")
            restaurante.save()
            return redirect('listar_restaurantes')
        else:
            logger.error("Errores en el formulario: %s", form.errors)
    else:
        form = RestauranteForm()
    return render(request, 'listar_restaurantes.html', {'form': form, 'restaurantes': Restaurante.objects.all()})

@login_required
def editar_restaurante(request, pk):
    restaurante = get_object_or_404(Restaurante, pk=pk)
    if request.method == "POST":
        form = RestauranteForm(request.POST, request.FILES, instance=restaurante)
        if form.is_valid():
            restaurante = form.save(commit=False)
            if 'imagen_url' in request.FILES:
                file = request.FILES['imagen_url']
                file_url = upload_to_s3(file, 'restaurantes')
                if file_url:
                    restaurante.imagen_url = file_url
            restaurante.save()
            return redirect('listar_restaurantes')
        else:
            return render(request, 'listar_restaurantes.html', {'form': form})
    else:
        form = RestauranteForm(instance=restaurante)
        return render(request, 'listar_restaurantes.html', {'form': form})

@login_required
def eliminar_restaurante(request, id):
    restaurante = get_object_or_404(Restaurante, pk=id)
    restaurante.delete()
    return redirect('listar_restaurantes')



from django.http import JsonResponse
#View para comentario 
def agregar_comentario(request):
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})

@login_required
def listar_comentarios(request):
    comentarios = Comentario.objects.all()
    return render(request, 'listar_comentarios.html', {'comentarios': comentarios})

@login_required
def eliminar_comentario(request, id):
    comentario = get_object_or_404(Comentario, id=id)
    comentario.delete()
    return redirect('listar_comentarios')

