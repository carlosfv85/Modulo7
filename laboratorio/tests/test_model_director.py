from laboratorio.models import DirectorGeneral

from django.test import TestCase


# Permite generar logs, que son mensajes de texto sobre el comportamiento del programa
import logging
 
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DirectorGeneralTest(TestCase):
    pass

    @classmethod
    def setUpTestData(cls) -> None:
        cls.director = DirectorGeneral(nombre= "Miguel García")
        cls.director.save()
        
    
    def test_model_content(self):
        """Nombre de la instancia / objeto corresponde al de la creación"""
        logger.info("Iniciando prueba: Nombre de la instancia / objeto corresponde al de la creación")
        self.assertEqual(self.director.nombre, "Miguel García")
        
    
    def test_verificacion_existencia(self):
        """Validar creación en DB de modelo DirectorGeneral"""
        logger.info("Iniciando prueba: creación en DB de modelo DirectorGeneral")
        
        director = DirectorGeneral.objects.get(id= self.director.id)
        
        self.assertEqual(director.nombre,self.director.nombre )
        
    
    def test_cambiar_nombre_director(self):
        """Validar creación en DB de modelo DirectorGeneral"""
        logger.info("Iniciando prueba: creación en DB de modelo DirectorGeneral")
        
        director = DirectorGeneral.objects.get(id= self.director.id)
        nuevo_nombre ="Pedro García"
        
        director.nombre = nuevo_nombre
        director.save()
        
        self.assertEqual(director.nombre, nuevo_nombre, "Nombre no coincide con lo esperado")
        
        
    def test_nombre_mayusculas(self):
        """Validar retorno función nombre_mayusculas"""
        logger.info("Iniciando prueba: retorno función nombre_mayusculas")
        
        nombre_mayusculas = self.director.nombre_mayusculas()
        nombre = self.director.nombre.upper()
        
        self.assertEqual(nombre_mayusculas, nombre)
        
        #Esta función arroja un error en su testing, porque no existe el metodo nombre_mayusculas
        #Para arreglar este problema se puede agregar el metodo en la clase del modelo (revisar clase)