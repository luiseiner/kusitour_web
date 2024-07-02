from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('somos/', views.somos, name='somos'),
    path('pregunta/', views.ingresar_comentario, name='pregunta'),
    path('login/', views.login_view, name='inicio_de_sesion'),

    # URLs para agencia
    path('administrador/', views.listar_agencias, name='listar_agencias'),
    path('agregar_agencia/', views.agregar_agencia, name='agregar_agencia'),
    path('editar_agencia/<int:id>/', views.editar_agencia, name='editar_agencia'),
    path('eliminar_agencia/<int:id>/', views.eliminar_agencia, name='eliminar_agencia'),
    
    # URLs para celebraciones
    path('celebraciones/', views.listar_celebraciones, name='listar_celebraciones'),
    path('agregar_celebracion/', views.agregar_celebracion, name='agregar_celebracion'),
    path('editar_celebracion/<int:pk>/', views.editar_celebracion, name='editar_celebracion'),
    path('eliminar_celebracion/<int:id>/', views.eliminar_celebracion, name='eliminar_celebracion'),

    # URLs para hoteles
    path('hoteles/', views.listar_hoteles, name='listar_hoteles'),
    path('agregar_hotel/', views.agregar_hotel, name='agregar_hotel'),
    path('editar_hotel/<int:pk>/', views.editar_hotel, name='editar_hotel'),
    path('eliminar_hotel/<int:id>/', views.eliminar_hotel, name='eliminar_hotel'),
    
    # URLs para lugares turísticos
    path('lugares_turisticos/', views.listar_lugares_turisticos, name='listar_lugares_turisticos'),
    path('agregar_lugar_turistico/', views.agregar_lugar_turistico, name='agregar_lugar_turistico'),
    path('editar_lugar_turistico/<int:pk>/', views.editar_lugar_turistico, name='editar_lugar_turistico'),
    path('eliminar_lugar_turistico/<int:id>/', views.eliminar_lugar_turistico, name='eliminar_lugar_turistico'),

    # URLs para restaurantes
    path('restaurantes/', views.listar_restaurantes, name='listar_restaurantes'),
    path('agregar_restaurante/', views.agregar_restaurante, name='agregar_restaurante'),
    path('editar_restaurante/<int:pk>/', views.editar_restaurante, name='editar_restaurante'),
    path('eliminar_restaurante/<int:id>/', views.eliminar_restaurante, name='eliminar_restaurante'),

    # URLs para comentarios
    path('agregar_comentario/', views.agregar_comentario, name='agregar_comentario'),
    path('listar_comentarios/', views.listar_comentarios, name='listar_comentarios'),
    path('eliminar_comentario/<int:id>/', views.eliminar_comentario, name='eliminar_comentario'),
]
