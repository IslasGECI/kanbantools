import numpy as np
from kanban_tools import calculate_five_numbers
from random import seed
import pandas as pd


seed(1)
data = [1, 2, 3, 4, 5]
data_101: np.array = np.arange(101)
d: dict = {"col1": [1, 2, 5, 8, 7]}
one_variable: pd.DataFrame = pd.DataFrame(data=d)
d2: dict = {"col1": [1, 2, 5, 8, 7], "col2": [1, 1, 1, 1, 1]}
two_variables: pd.DataFrame = pd.DataFrame(data=d2)
column_name_expected = [
    "Nombre_de_la_categoria",
    "Cantidad_de_datos",
    "Promedio",
    "Desviacion_estandar",
    "Minimo_de_la_muestra",
    "Cuartil_inferior",
    "Valor_medio",
    "Cuartil_superior",
    "Maximo_de_la_muestra",
]


def test_quantiles_25_50_75():
    """
    Sacar los cuantiles 25, 50 y 75% del numero de tareas de clase 3
    """
    expected_output = [2, 3, 4]
    np.testing.assert_array_equal(calculate_five_numbers.quantiles_25_50_75(data), expected_output)


def test_ic_95():
    """
    Sacar los cuantiles intervalo de credibilidad del 95 porciento
    """
    expected_output_101: np.array = np.array([2.5, 97.5])
    obtained_output_101: np.array = calculate_five_numbers.ic_95(data_101)
    np.testing.assert_array_equal(obtained_output_101, expected_output_101)


def test_five_numbers():
    assert_five_numbers(data, data)
    expected_five_numbers_101: np.array = np.array([0, 25, 50, 75, 100])
    assert_five_numbers(data_101, expected_five_numbers_101)


def assert_five_numbers(datos, expected_five_numbers):
    obtained_five_numbers: np.array = calculate_five_numbers.five_numbers(datos)
    np.testing.assert_array_equal(obtained_five_numbers, expected_five_numbers)


def test_dimension_table_AED():
    """
    Revisa la forma del data frame del AED. Vamos a tener 9 columnas y una fila
    por cada variable del data frame.
    """
    tabla_aed = calculate_five_numbers.table_AED(one_variable)
    index = tabla_aed.index
    obtained_number_of_rows = len(index)
    expected_number_of_rows = len(one_variable.columns)
    assert expected_number_of_rows == obtained_number_of_rows

    tabla_aed = calculate_five_numbers.table_AED(two_variables)
    index = tabla_aed.index
    obtained_number_of_rows = len(index)
    expected_number_of_rows = len(two_variables.columns)
    assert expected_number_of_rows == obtained_number_of_rows

    index = tabla_aed.columns
    number_of_columns = len(index)
    assert number_of_columns == 9


def test_names_table_AED():
    tabla_aed = calculate_five_numbers.table_AED(one_variable)
    assert tabla_aed.iloc[0, 0] == "col1"
    column_name_obtained = tabla_aed.columns.values.tolist()
    assert column_name_expected == column_name_obtained
