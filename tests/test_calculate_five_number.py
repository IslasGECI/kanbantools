import unittest
from kanban_tools import *
from random import seed

class TestFiveNumbers(unittest.TestCase):
    def setUp(self):
        """
        Crea variables que se usarán en las pruebas
        """
        seed(1)

    def test_quantiles_25_50_76(self):
        """
        Sacar los cuantiles 25, 50 y 75% del numero de tareas de clase 3
        """

if __name__ == '__main__':
    unittest.main()