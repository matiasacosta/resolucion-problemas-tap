import unittest
from notas import notas

class TestClass(unittest.TestCase):

    """Test case docstring."""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_notas(self):
        self.assertEqual(notas.get_nota(2, "MI"), "RE")
        self.assertEqual(notas.get_nota(2, "DO"), "LA#")
        self.assertEqual(notas.get_nota(3, "SOL#"), "FA")
        self.assertEqual(notas.get_nota(3, "DO#"), "LA#")
