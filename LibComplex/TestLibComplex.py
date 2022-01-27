import libcplx as lc
import unittest

class TestStringMethods(unittest.TestCase):

    def test_suma_compleja(self):
        self.assertEqual(lc.suma((5,5),(-1.7,3.4)),(3.3,8.4))

    def test_resta_compleja(self):
        self.assertEqual(lc.resta((5,5),(-1.7,3.4)),(3.3,8.4))

    def test_multiplicacion_compleja(self):
        self.assertEqual(lc.multiplicacion((5,5),(-1.7,3.4)),(3.3,8.4))

if __name__ == '__main__':
    unittest.main()
