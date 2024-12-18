import datetime
from django.db import models
 
# Create your models here.
class DirectorGeneral(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    especialidad = models.CharField(max_length=50, null=True, blank=True)
   
    def __str__(self):
        return self.nombre
    
    #Se agrega metodo para funcionamiento de prueba en testing
    def nombre_mayusculas(self):
        return self.nombre.upper()
 
    class Meta:
        managed = True
        db_table = 'directores_generales'
 
 
class Laboratorio(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    director = models.OneToOneField(DirectorGeneral, on_delete=models.CASCADE, unique=True, null=True, blank=True)
    ciudad = models.CharField(max_length=50, null= True, blank=True)
    pais = models.CharField(max_length=50, null=True, blank=True)
   
    def __str__(self):
        return self.nombre
 
    class Meta:
        managed = True
        db_table = 'laboratorios'
       
 
def anio_actual():
        return int(datetime.date.today().year)
 

class Producto(models.Model):
    anios_choices = [
        (anio, str(anio)) for anio in range(2015, anio_actual()+1)
    ]
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.SET_NULL, blank=True, null=True)
    f_fabricacion = models.IntegerField(choices=anios_choices, default=anio_actual())
    precio_costo =  models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, default=0)
    precio_venta =  models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, default=9999999)
   
    def __str__(self):
        return self.nombre
 
    class Meta:
        managed = True
        db_table = 'productos'
       

class Pagina(models.Model):
    nombre = models.CharField(max_length=50, unique=True) 
    cuenta_vistas = models.PositiveIntegerField(default=0) 

    def __str__(self):
        return f"{self.nombre}: {self.cuenta_vistas} visitas"
    
    def incrementar_visitas(self):
        self.cuenta_vistas += 1
        self.save()