from dash import Dash, dash_table
import pandas as pd
from collections import OrderedDict

from matplotlib import pyplot as plt


def sum_of_elements_vertical(idx, arr):
    result = 0

    for row in arr:
        result += row[idx]

    return result


def task_one():
    a = 0.05
    input = [
        [7, 5, 7, 9],
        [8, 9, 9, 12],
        [10, 11, 12, 14],
        [12, 12, 14, 16],
        [13, 13, 18, 19],
    ]
    xgr = [10, 10, 12, 14]

    help_data = []
    for row in input:
        res = []
        for n in row:
            res.append(n)
            res.append(n ** 2)

        help_data.append(res)

    help_data.append([
        0,
        sum_of_elements_vertical(1, help_data),
        0,
        sum_of_elements_vertical(3, help_data),
        0,
        sum_of_elements_vertical(5, help_data),
        0,
        sum_of_elements_vertical(7, help_data),
    ])
    help_data.append([
        sum_of_elements_vertical(0, help_data),
        0,
        sum_of_elements_vertical(2, help_data),
        0,
        sum_of_elements_vertical(4, help_data),
        0,
        sum_of_elements_vertical(6, help_data),
        0,
    ])
    help_data.append([
        help_data[-1][0] ** 2,
        0,
        help_data[-1][2] ** 2,
        0,
        help_data[-1][4] ** 2,
        0,
        help_data[-1][6] ** 2,
        0,
    ])

    for row in help_data:
        print(row)

    m = len(input[0])
    s = len(input)

    print(f"m = {m}")
    print(f"s = {s}")

    s_total = 2898 - (1 / (m * s)) * (230 ** 2)
    print(f"s_total = {s_total}")

    s_actual = 13500 / s - (230 ** 2) / (m * s)
    print(f"s_actual = {s_actual}")

    s_remainder = s_total - s_actual
    print(f"s_remainder = {s_remainder}")

    s2_actual = round(s_actual / (m - 1), 2)
    print(f"s2_actual = {s2_actual}")

    s2_remainder = round(s_remainder / (m * (s - 1)), 2)
    print(f"s2_remainder = {s2_remainder}")

    f_obs = round(s2_actual / s2_remainder, 3)
    print(f"f_obs = {f_obs}")

    k1 = m - 1
    k2 = m * (s - 1)
    f_cr = 3.24  # З таблиці Фишера - Снедекора
    print(f"Fcr({a}, {k1}, {k2}) = {f_cr}")
    print(f"Hypothesis is true: {f_obs < f_cr}")


def task_two():
    a = 0.01
    n = 18
    m = 4

    s_total = 11954 - (1 / n) * (438 ** 2)
    print(f"s_total = {s_total}")

    s_actual = ((135 ** 2 / 5) + (100 ** 2 / 4) + (156 ** 2 / 6) + (69 ** 2 / 3)) - (1 / n) * (438 ** 2)
    print(f"s_actual = {s_actual}")

    s_remainder = s_total - s_actual
    print(f"s_remainder = {s_remainder}")

    s2_actual = round(s_actual / (m - 1), 2)
    print(f"s2_actual = {s2_actual}")

    s2_remainder = round(s_remainder / (n - m), 2)
    print(f"s2_remainder = {s2_remainder}")

    f_obs = round(s2_actual / s2_remainder, 3)
    print(f"f_obs = {f_obs}")

    k1 = m - 1
    k2 = n - m
    print(f"k1 = {k1}")
    print(f"k2 = {k2}")
    f_cr = 5.56  # З таблиці Фишера - Снедекора
    print(f"Fcr({a}, {k1}, {k2}) = {f_cr}")
    print(f"Hypothesis is true: {f_obs < f_cr}")





if __name__ == '__main__':
    task_one()
    task_two()
