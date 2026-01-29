import unittest
from src.calculadora import suma, resta, multiplicacion, division

class TestCalculadora(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(suma(2, 3), 5)

    def test_resta(self):
        self.assertEqual(resta(5, 3), 2)

    def test_multiplicacion(self):
        self.assertEqual(multiplicacion(4, 2), 8)

    def test_division(self):
        self.assertEqual(division(10, 2), 5)

    def test_division_por_cero(self):
        self.assertEqual(division(5, 0), "Error: división por cero")

if __name__ == "__main__":
    unittest.main()

