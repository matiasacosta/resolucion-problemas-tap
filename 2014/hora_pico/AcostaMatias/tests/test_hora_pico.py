import unittest
from  import main.get_cant_turnos

class TestHoraPico(unittest.TestCase):
    """
    Este test me permite corroborar que la solución es correcta
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_hora_pico(self):
        self.assertEqual(get_cant_turnos(5, [4,5,2,3,1]), 3)
        self.assertEqual(get_cant_turnos(3, [1,2,3]), 1)
        self.assertEqual(get_cant_turnos(9, [9,4,2,7,8,3,5,6,1]),4)


