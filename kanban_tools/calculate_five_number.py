import numpy as np
import pandas as pd


def quantiles_25_50_75(data):
    return np.percentile(data, [25, 50, 75])


def ic_95(data):
    return np.percentile(data, [2.5, 97.5])


def five_number(data):
    return np.percentile(data, [0, 25, 50, 75, 100])


def table_AED(data):
    columns_dict = {
        "index": "Nombre_de_la_categoria",
        "count": "Cantidad_de_datos",
        "mean": "Promedio",
        "std": "Desviacion_estandar",
        "min": "Minimo_de_la_muestra",
        "25%": "Cuartil_inferior",
        "50%": "Valor_medio",
        "75%": "Cuartil_superior",
        "max": "Maximo_de_la_muestra",
    }
    summary_table = data.describe().T
    summary_table.reset_index(inplace=True)
    return summary_table.rename(columns = columns_dict)
