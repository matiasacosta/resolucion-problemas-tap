import unittest
from cuadrados import cuadrados

class TestCuadrados(unittest.TestCase):

    """Test case docstring."""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_cuadrados(self):
        self.assertEqual(cuadrados.cuadrado(1), 1)
        self.assertEqual(cuadrados.cuadrado(2), 5)
        self.assertEqual(cuadrados.cuadrado(3), 14)
        self.assertEqual(cuadrados.cuadrado(8), 204)
