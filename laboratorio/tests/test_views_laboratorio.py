from django.test import TestCase
from django.urls import reverse
 
import logging
 
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
 
 
class LaboratorioViewTests(TestCase):
   
    @classmethod
    def setUpTestData(cls):
       pass
       
    def test_page_laboratorios(self):
        """Verificador código respuesta HTTP 200 de vista laboratorios"""
        logger.info("Iniciando prueba: Verificación código respuesta HTTP 200 en vista laboratorios.")
       
        response = self.client.get(reverse("laboratorios"))
        self.assertEqual(response.status_code, 200, "Código de respueta de la vista no coincide con el código 200")
    
    
    def test_page_laboratorios(self):
        """Verificar nombre template 'laboratorios.html'"""
        logger.info("Iniciando prueba: Verificar nombre template 'laboratorios.html'")
       
        response = self.client.get(reverse("laboratorios"))
        self.assertTemplateUsed(response, "laboratorios.html")
        
        
    
    def test_contexto_laboratorios(self):
        """Verificar contenido contexto laboratorios"""
        logger.info("Iniciando prueba: Verificar contenido contexto laboratorios")
       
        response = self.client.get(reverse("laboratorios"))
        
        self.assertIn('laboratorios', response.context, "No existe una clave llamada laboratorios en el contexto de la vista")
        
        
    
    def test_verificacion_titulo_template(self):
        """Verificar el titulo del documento del template de la vista laboratorios"""
        logger.info("Iniciando prueba: Verificar el titulo del documento del template de la vista laboratorios")
       
        response = self.client.get(reverse("laboratorios"))
        
        self.assertContains(response, "<title>Laboratorios</title>", html=True )