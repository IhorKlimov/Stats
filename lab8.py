import math

from matplotlib import pyplot as plt
from scipy import integrate


def find_occurrences(arr):
    result = {}
    for n in arr:
        if n in result:
            result[n] = result[n] + 1
        else:
            result[n] = 1

    return dict(sorted(result.items()))


def sum_of_elements_vertical(idx, arr):
    result = 0

    for row in arr:
        result += row[idx]

    return result


def get_size_of_selection(occurrences):
    n = 0
    for ni in occurrences.values():
        n += ni

    return n


def get_xb(occurrences):
    sum_of_elements = 0
    for z in occurrences:
        sum_of_elements += z * occurrences[z]

    n = get_size_of_selection(occurrences)
    return 1 / n * sum_of_elements


def get_db(occurrences):
    xb = get_xb(occurrences)

    db_sum = 0
    for z in occurrences:
        db_sum += (z - xb) ** 2 * occurrences[z]

    db = 1 / get_size_of_selection(occurrences) * db_sum
    return db


def get_laplas(x):
    if x == "-∞":
        return -0.5
    elif x == "+∞":
        return 0.5
    else:
        return round((1 / math.sqrt(2 * math.pi)) * integrate.quad(lambda x: math.e ** ((-x ** 2) / 2), 0, x)[0], 4)


def get_s2(occurrences):
    xb = get_xb(occurrences)
    n = get_size_of_selection(occurrences)
    db_sum = 0
    for z in occurrences:
        db_sum += (z - xb) ** 2 * occurrences[z]

    db = 1 / n * db_sum

    return n / (n - 1) * db


def get_help_data_zi_interval(start, h, k, xb, sigma_b, n):
    result = []

    for i in range(k):
        zi = round(start + h * i, 2)
        zi_plus_one = round(zi + h, 2)
        ui = "-∞" if i == 0 else round((zi - xb) / sigma_b, 2)
        ui_plus_one = "+∞" if i == k - 1 else round((zi_plus_one - xb) / sigma_b, 2)
        row = [
            i + 1,
            zi,
            zi_plus_one,
            ui,
            ui_plus_one,
            get_laplas(ui),
            get_laplas(ui_plus_one),
            round(n * (get_laplas(ui_plus_one) - get_laplas(ui)), 2)
        ]

        result.append(row)

    return result


def get_help_data_ni_interval(start, h, k, xb, sigma_b, n, interval_occurrences):
    result = []
    sum_ni = 0
    x_2_obs = 0

    for i in range(k):
        zi = round(start + h * i, 2)
        zi_plus_one = round(zi + h, 2)
        ui = round((zi - xb) / sigma_b, 2)
        ui_plus_one = round((zi_plus_one - xb) / sigma_b, 2)

        ni = interval_occurrences[i]
        sum_ni += ni
        ni_quote = round(n * (get_laplas(ui_plus_one) - get_laplas(ui)), 2)
        last = round(((ni - ni_quote) ** 2) / ni_quote, 4)
        x_2_obs += last
        row = [
            i + 1,
            ni,
            ni_quote,
            round(ni - ni_quote, 2),
            round((ni - ni_quote) ** 2, 4),
            last
        ]

        result.append(row)

    result.append([
        "Σ", sum_ni, sum_ni, "", "", f"x^2сп = {round(x_2_obs, 2)}"
    ])

    return result


def task_one():
    h = 1  # Розмір інтервалів
    k = 10
    start = 1
    interval_occurrences = [52, 45, 29, 26, 24, 20, 16, 13, 11, 8]
    discrete_zi = []
    occurrences = {}
    for i in range(k):
        left = start + i * h
        z = left + h / 2
        discrete_zi.append(z)
        occurrences[z] = interval_occurrences[i]

    print(discrete_zi)
    print(interval_occurrences)
    print(occurrences)

    zi = list(occurrences.keys())
    ni = list(occurrences.values())

    fig, ax = plt.subplots()
    ax.spines[["left", "bottom"]].set_position(("data", 0))
    ax.spines[["top", "right"]].set_visible(False)
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    ax.plot(zi, ni, marker='o')
    plt.ylabel('ni')
    plt.xlabel('zi')
    plt.xticks(zi)
    plt.yticks(ni)
    ax.vlines(zi, 0, ni, linestyle="dashed", linewidth=1.0)
    ax.hlines(ni, 0, zi, linestyle="dashed", linewidth=1.0)
    plt.show()

    xb = get_xb(occurrences)
    db = get_db(occurrences)
    sigma_b = math.sqrt(db)

    print(f"xb = {xb}")
    print(f"db = {db}")
    print(f"sigma b = {sigma_b}")

    fig, ax = plt.subplots()
    data = get_help_data_zi_interval(start, h, k, xb, sigma_b, get_size_of_selection(occurrences))
    ax.axis('tight')
    ax.axis('off')
    ax.table(cellText=data, loc="center", cellLoc="center",
             colLabels=["i", "zi", "zi+1", "ui", "ui+1", "φ(ui)", "φ(ui+1)", "ni'"])
    plt.show()

    fig, ax = plt.subplots()
    data = get_help_data_ni_interval(start, h, k, xb, sigma_b, get_size_of_selection(occurrences), interval_occurrences)
    ax.axis('tight')
    ax.axis('off')
    ax.table(cellText=data, loc="center", cellLoc="center",
             colLabels=[
                 "i", "ni", "ni'", "ni - ni'", "(ni - ni')^2",
                 r'$\dfrac{{{}}}{{{}}}$'.format("(ni - ni')^2", "ni'")
             ])
    plt.show()

    k = len(interval_occurrences) - 3
    print(f"k = {k}")
    x_2_cr = 18.5  # Знайшов с таблиці x^2(0.01, 7)


def get_task_two_help_data(index, arr):
    occurrences = find_occurrences(arr)
    n = len(arr)
    k = n - 1
    s2 = get_s2(occurrences)

    return [
        index,
        n,
        k,
        round(s2, 1),
        round(k * s2, 1),
        round(math.log10(s2), 4),
        round(k * math.log10(s2), 4),
        round(1 / k, 4)
    ]


def task_two():
    arr_1 = [1, 2, 11, 1, 4, 6, 10, 5, 19, 10]
    arr_2 = [6, 11, 5, 20, 15, 3, 13, 11, 9, 12, 5]
    arr_3 = [9, 6, 11, 12, 11, 19, 15, 12, 9, 3, 9, 6, 14, 19]
    arr_4 = [6, 10, 9, 18, 7, 3, 14, 2, 11, 16, 6, 5, 18, 12, 2, 2, 11, 3]
    a = 0.05

    data = []
    data.append(get_task_two_help_data(1, arr_1))
    data.append(get_task_two_help_data(2, arr_2))
    data.append(get_task_two_help_data(3, arr_3))
    data.append(get_task_two_help_data(4, arr_4))

    k = sum_of_elements_vertical(2, data)
    s2_over = round(sum_of_elements_vertical(4, data) / k, 2)

    data.append([
        "",
        "",
        f"k = {k}",
        "",
        r"$\overline{s^2} = $" + str(s2_over),
        "",
        round(sum_of_elements_vertical(6, data), 4),
        round(sum_of_elements_vertical(7, data), 4)
    ])

    fig, ax = plt.subplots()
    ax.axis('tight')
    ax.axis('off')
    ax.table(cellText=data, loc="center", cellLoc="center",
             colLabels=["i", "ni", "ki", "si^2", "ki*si^2", "lgsi^2", "ki*lgsi^2", "1/ki"])
    plt.show()

    sum_klgs2 = data[-1][6]
    sum_1overk = data[-1][7]
    m = 4

    b_obs = (2.303 * (k * math.log10(s2_over) - sum_klgs2)) / (1 + (1 / (3 * (m - 1))) * (sum_1overk - (1 / k)))
    print(f"b obs = {round(b_obs, 4)}")

    x2_cr = 7.8  # Знайшов з таблиці x^2(0.05, 3)


def get_k_for(i, arr1, arr2, merged):
    n = merged[i]

    if n in arr1 and n in arr2:
        count = 0
        sum = 0
        for idx, nm in enumerate(merged):
            if nm == n:
                sum += idx + 1
                count += 1

        return sum / count
    else:
        return i + 1


def task_three():
    a = 0.05
    arr1 = sorted(
        [5, 15, 20, 15, 8, 9, 5, 8, 2, 12, 16, 10, 17, 10, 1, 19, 9, 12, 12, 8, 7, 4, 5, 1, 8, 6, 3, 9, 17, 13])
    arr2 = sorted([3, 15, 17, 20, 17, 17, 5, 9, 11, 11, 14, 13, 10, 8, 6, 6, 12, 11, 1, 14])

    print(arr1)
    print(arr2)
    merged = sorted(arr1 + arr2)

    data = []

    l = math.ceil(len(merged) / 3)
    print(l)
    for i in range(l):
        i3 = l * 2 + i
        i2 = merged[l + i]

        data.append([
            merged[i],
            get_k_for(i, arr1, arr2, merged),
            i2,
            get_k_for(i2, arr1, arr2, merged),
            merged[i3] if i3 <= len(merged) - 1 else "",
            get_k_for(i3, arr1, arr2, merged) if i3 <= len(merged) - 1 else "",
        ])

    inline_data = []
    for idx, n in enumerate(merged):
        inline_data.append(get_k_for(idx, arr1, arr2, merged))

    print(inline_data)

    fig, ax = plt.subplots()
    ax.axis('tight')
    ax.axis('off')
    ax.table(cellText=data, loc="center", cellLoc="center",
             colLabels=["Варіанта", "Порядковий номер", "Варіанта", "Порядковий номер", "Варіанта", "Порядковий номер"])
    plt.show()

    w_obs = 0
    for idx, n in enumerate(arr2):
        w_obs += inline_data[idx]

    print(f"w_obs = {w_obs}")

    f_zcr = (1 - 2 * a) / 2
    print(f"F_zcr = {f_zcr}")
    zcr = 1.645  # З таблиці Лапласа
    n1 = len(arr2)
    n2 = len(arr1)
    w_low = ((n1 + n2 + 1) * n1 - 1) / 2 - zcr * math.sqrt((n1 * n2 * (n2 + n1 + 1)) / 12)
    print(f"w_low = {w_low}")
    w_high = (n1 + n2 + 1) * n1 - w_low
    print(f"w_high = {w_high}")
    print(f"Hypothesis is true {w_obs < w_high}")


if __name__ == '__main__':
    task_one()
    task_two()
    task_three()
