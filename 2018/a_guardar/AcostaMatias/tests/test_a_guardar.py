import unittest
from movimientos import get_camino_corto

class TestAGuardar(unittest.TestCase):
    """
    Este test me permite corroborar que la solución es correcta
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_a_guardar(self):
        self.assertEqual(get_camino_corto(
            (4,4), ["#.##", "..##", "..##", ".E.C"]
        ),(4,'LLURD'))
        self.assertEqual(get_camino_corto(
            (4,8), ["........", "..C..E..", "........", "........"]
        ),(2,'RR'))
        self.assertEqual(get_camino_corto(
            (3,4), [".C..", ".E#.", "...."]
        ),(-1,''))