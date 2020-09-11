import numpy as np
from kanban_tools import calculate_five_number
from random import seed
import pandas as pd


seed(1)
data = [1, 2, 3, 4, 5]
expected_output = [2, 3, 4]
data_101: np.array = np.arange(101)
expected_output_101: np.array = np.array([2.5, 97.5])
expected_five_number_101: np.array = np.array([0, 25, 50, 75, 100])
d: dict = {"col1": [1, 2, 5, 8, 7]}
df: pd.DataFrame = pd.DataFrame(data=d)
column_name_expected = ["Nombre_de_la_categoria", "Cantidad_de_datos", "Promedio", "Desviacion_estandar", "Minimo_de_la_muestra", "Cuartil_inferior", "Valor_medio", "Cuartil_superior","Maximo_de_la_muestra"]


def test_quantiles_25_50_75():
    """
    Sacar los cuantiles 25, 50 y 75% del numero de tareas de clase 3
    """
    np.testing.assert_array_equal(calculate_five_number.quantiles_25_50_75(data), expected_output)


def test_ic_95():
    """
    Sacar los cuantiles intervalo de credibilidad del 95 porciento
    """
    np.testing.assert_array_equal(calculate_five_number.ic_95(data_101), expected_output_101)


def test_five_number():
    np.testing.assert_array_equal(calculate_five_number.five_number(data), data)
    np.testing.assert_array_equal(
        calculate_five_number.five_number(data_101), expected_five_number_101
    )


def test_table_AED():
    """
    Revisa la forma y nombre de las columnas del data frame del AED
    """
    tabla_aed = calculate_five_number.table_AED(df)
    index = tabla_aed.index
    number_of_rows = len(index)
    assert number_of_rows == 1
    index = tabla_aed.columns
    number_of_columns = len(index)
    assert number_of_columns == 9
    assert tabla_aed.ilog[0,0] == "col1"
    column_name_obtained = tabla_aed.columns.values.tolist()
    assert column_name_expected == column_name_obtained
