class Calculadora:
    def sumar(self, a, b):
       
        if  not isinstance(a,  int) or not isinstance(b,  int):
                raise ValueError("No se pueden sumar valores que no sean números")
           
        try:
           
            a = int(a)
            b = int(b)
           
            return a+b
        except Exception as e:
            raise "Error en operación de suma"
 
# CÓDIGO DE TESTING
from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse
 
import logging
 
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
 
 
class CalculadoraTest(TestCase):
    def setUp(self):
        self.calculadora = Calculadora()
   
    def test_suma_dos_numeros_positivos(self):
        """Prueba de suma de dos números positivos"""
        logger.info("Iniciando prueba: Suma de 2 números positivos")
        resultado = self.calculadora.sumar(3, 5)
        self.assertEqual(resultado, 8, "El resultado esperado es 8.")
   
    def test_suma_dos_valores_no_numericos(self):
        """Prueba de validación de suma con 2 números strings"""
        logger.info("Iniciando prueba: Suma con 2 números strings")
        resultado = self.calculadora.sumar("3", "5")
        self.assertEqual(resultado, 8, "El resultado esperado es 8.")
       
       
    def test_comportamiento_suma_valores_no_numericos(self):
        """Prueba para validar comportamiento de la función ante paso de valores no números. Ejemplo: 'a' + 'b'"""
        logger.info("Iniciando prueba: Validación de suma de valores no números")
 
   
        with self.assertRaises(ValueError) as context:
            self.calculadora.sumar("a", "b")
           
        mensaje_error = str(context.exception)
        mensaje_esperado = "No se pueden sumar valores que no sean números"
 
        self.assertEqual(mensaje_error, mensaje_esperado)