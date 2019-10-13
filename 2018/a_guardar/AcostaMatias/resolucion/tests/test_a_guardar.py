import unittest
from resolucion.Caja import resolucion


class TestAGuardar(unittest.TestCase):
    """
    Este test me permite corroborar que la solución es correcta
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_a_guardar(self):
        # Test 1
        camino = resolucion(["#.##", "..##", "..##", ".E.C"])
        self.assertEqual(len(camino), 4)
        self.assertEqual(camino, 'LLURD')
        # Test 2
        camino = resolucion(["........", "..C..E..", "........", "........"])
        self.assertEqual(len(camino), 2)
        self.assertEqual(camino, 'RR')
        # Test 3
        camino = resolucion([".C..", ".E#.", "...."])
        self.assertEqual(camino, False)


if __name__ == '__main__':
    unittest.main()
