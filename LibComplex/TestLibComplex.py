import libcplx as lc
import unittest

'''

PRUEBAS DE UNIDAD, LIBRERIA NUMEROS COMPLEJOS

ELABORADO POR: JOSE RICARDO OLARTE PARDO

'''

#Clase para pruebas de unidad
class TestStringMethods(unittest.TestCase):

    #Test de suma de un numero complejo
    def test_suma_compleja(self):
        self.assertEqual(lc.suma((5,5),(-1.7,3.4)),(3.3,8.4))
        self.assertEqual(lc.suma((4,4),(-1.7,3.4)),(2.3,7.4))
        self.assertEqual(lc.suma((3,3),(-1.7,3.4)),(1.3,6.4))

    #Test de resta de un numero complejo
    def test_resta_compleja(self):
        self.assertEqual(lc.resta((5,5),(-1.7,3.4)),(6.7,1.6))
        self.assertEqual(lc.resta((4,4),(-1,1)),(5,3))
        self.assertEqual(lc.resta((0,0),(-1.7,3.4)),(1.7,-3.4))

    #Test de conjugado de un numero complejo
    def test_conjugado_compleja(self):
        self.assertEqual(lc.conjugado((-1.7,3.4)),(-1.7,-3.4))
        self.assertEqual(lc.conjugado((1.7,-3.4)),(1.7,3.4))
        self.assertEqual(lc.conjugado((99999,-1)),(99999,1))
    
    #Test de multiplicacion de un numero complejo
    def test_multiplicacion_compleja(self):
        self.assertEqual(lc.multiplicacion((5,5),(-1.7,3.4)),(-25.5,8.5))

    #Test de division de un numero complejo
    def test_division_compleja(self):
        self.assertEqual(lc.division((2,1),(-1,1)),(-0.5,-1.5))

    #Test de modulo de un numero complejo
    def test_modulo_compleja(self):
        self.assertEqual(lc.modulo((4,3)),5)
    
    #Test de fase de un numero complejo
    def test_fase_compleja(self):
        self.assertEqual(lc.fase((3,7)),66.8)
        
    #Test de coordenada polar de un numero complejo
    def test_polar_compleja(self):
        self.assertEqual(lc.polar((-1.5,3)),(3.35,63.43))

    #Test de coordena cartesiana de un numero complejo
    def test_cartesiana_compleja(self):
        self.assertEqual(lc.cartesiana((-1.5,3)),(1.4849887449006682,-0.2116800120898008))
        
#Main
if __name__ == '__main__':
    unittest.main()
