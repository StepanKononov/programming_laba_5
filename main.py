import pandas as pd
import numpy as np
import data_proocessing as data_p
from prettytable import PrettyTable
import openpyxl


# start, stop, step = map(float, input().split())


def fun_1(x):
    return np.sin(x) + 0.1 * np.sin(x ** 5)


def fun_2(x):
    return np.sin(x) * np.sin(x ** 2)


def fun_3(x):
    return np.cos(x)


def laba_processing(function, titel, excel_write=False):
    deviation_table = PrettyTable()
    deviation_table.title = titel
    deviation_table.field_names = ["Суммарное отклонение", "Начало", "Конец", "Шаг"]

    def det_data(start, stop, step, function):

        data = []
        x = start
        while x < stop:
            data.append(function(x))
            x += step
        deviation_table.add_row([data_p.deviation(data_p.prediction(data, 2, 2), data), start, stop, step])
        return data

    data_1 = det_data(0, 2, 0.01, function)
    data_2 = det_data(0, 2, 0.001, function)
    data_3 = det_data(0, 2, 0.0001, function)
    print(deviation_table)

    if excel_write:
        df = pd.DataFrame(data_1, columns=["Data"])
        smooth_df = pd.DataFrame(data_p.smoothing(data_1), columns=["Smooth data"])
        prediction_df = pd.DataFrame(data_p.prediction(data_1, 2, 2), columns=["Prediction data"])

        with pd.ExcelWriter("Excel.xlsx",
                            mode="a",
                            engine="openpyxl",
                            if_sheet_exists="overlay",
                            ) as writer:
            df.to_excel(writer, sheet_name="Sheet1")
            smooth_df.to_excel(writer, sheet_name="Sheet1", startcol=3)
            prediction_df.to_excel(writer, sheet_name="Sheet1", startcol=7)


laba_processing(fun_1, "Функция №1", excel_write=True)
laba_processing(fun_2, "Функция №2")
laba_processing(fun_3, "Функция №3")
