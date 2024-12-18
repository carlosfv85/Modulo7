from django.contrib import admin

from .models import Laboratorio, DirectorGeneral, Producto

# Register your models here.

class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)
    list_filter = ('director',)
     

    
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'laboratorio','f_fabricacion', 'precio_costo', 'precio_venta')
    search_fields = ('nombre',)
    list_filter = ('laboratorio',)
    

    
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'laboratorio')
    search_fields = ('nombre',)
    list_filter = ('laboratorio',)
    

admin.site.register(Laboratorio, LaboratorioAdmin)    
admin.site.register(Producto, ProductoAdmin)    
admin.site.register(DirectorGeneral, DirectorAdmin)

