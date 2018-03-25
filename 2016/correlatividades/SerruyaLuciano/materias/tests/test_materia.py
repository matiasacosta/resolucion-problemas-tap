import unittest
from materias.materia.Materia import Materia

class TestClass(unittest.TestCase):
    """ Tests para las materias y correlatividades """

    def setUp(self):
        self.m1 = Materia(1)
        self.m2 = Materia(2)
        self.m2.agregar_correlativa(self.m1)
        self.m3 = Materia(3)
        self.m3.agregar_correlativa(self.m2)

    def tearDown(self):
        pass

    def test_sin_correlatividades_registrable(self):
        self.m1.aprobar()
        self.assertTrue(self.m1.sos_registrable())

    def test_con_correlatividades_no_registrable(self):
        self.m2.aprobar()
        self.assertFalse(self.m2.sos_registrable())

    def test_con_correlatividades_registrable(self):
        self.m1.aprobar()
        self.m2.aprobar()
        self.assertTrue(self.m2.sos_registrable())

    def test_correlativa_faltante(self):
        self.m1.aprobar()
        self.m3.aprobar()
        self.assertFalse(self.m3.sos_registrable())

    def test_otra_correlativa_faltante(self):
        self.m2.aprobar()
        self.m3.aprobar()
        self.assertFalse(self.m3.sos_registrable())

    def test_multiples_correlativas(self):
        self.m1.aprobar()
        self.m2.aprobar()
        self.m3.aprobar()
        self.assertTrue(self.m3.sos_registrable())
