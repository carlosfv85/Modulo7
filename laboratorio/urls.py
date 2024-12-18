from django.urls import path
from . import views


urlpatterns = [
    path('laboratorios/', views.laboratorios, name="laboratorios"),
    path('laboratorios/crear', views.crear_laboratorio, name="crear_laboratorio"),
    path('laboratorios/editar/<int:laboratorio_id>/', views.editar_laboratorio, name='editar_laboratorio'),
    path('laboratorios/eliminar/<int:laboratorio_id>/', views.eliminar_laboratorio, name='eliminar_laboratorio'),
]
