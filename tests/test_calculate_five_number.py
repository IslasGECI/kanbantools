import unittest
from kanban_tools import *
from random import seed

class TestFiveNumbers(unittest.TestCase):
    def setUp(self):
        """
        Crea variables que se usarán en las pruebas
        """
        seed(1)
        self.data=[1,2,3,4,5]
        self_expected_output=[2,3,4]

    def test_quantiles_25_50_75(self):
        """
        Sacar los cuantiles 25, 50 y 75% del numero de tareas de clase 3
        """
        self.assertEqual(quantiles_25_50_75(self.data), self.expected_output)

if __name__ == '__main__':
    unittest.main()