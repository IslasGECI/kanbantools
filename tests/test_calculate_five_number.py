import unittest
import numpy as np
from kanban_tools import calculate_five_number
from random import seed


class TestFiveNumbers(unittest.TestCase):
    def setUp(self):
        """
        Crea variables que se usarán en las pruebas
        """
        seed(1)
        self.data = [1, 2, 3, 4, 5]
        self.expected_output = [2, 3, 4]
        self.data_101: np.array = np.arange(101)
        self.expected_output_101: np.array = np.array([2.5, 97.5])

    def test_quantiles_25_50_75(self):
        """
        Sacar los cuantiles 25, 50 y 75% del numero de tareas de clase 3
        """
        np.testing.assert_array_equal(calculate_five_number.quantiles_25_50_75(self.data), self.expected_output)

    def test_ic_95(self):
        """
        Sacar los cuantiles 25, 50 y 75% del numero de tareas de clase 3
        """
        np.testing.assert_array_equal(calculate_five_number.ic_95(self.data_101), self.expected_output_101)


if __name__ == "__main__":
    pytest.main()