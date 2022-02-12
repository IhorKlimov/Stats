import math

from matplotlib import pyplot as plt
import scipy.integrate as integrate


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


def find_occurrences(arr):
    result = {}
    for n in arr:
        if n in result:
            result[n] = result[n] + 1
        else:
            result[n] = 1

    return dict(sorted(result.items()))


def get_size_of_selection(occurrences):
    n = 0
    for ni in occurrences.values():
        n += ni

    return n


def get_n_within_interval(occurrences, left, right):
    result = 0

    for idx, z in enumerate(occurrences):
        n = occurrences[z]

        if left < z < right:
            result += n
        elif z == left:
            if idx == 0:
                # Take all, as it's the left edge
                result += n
            else:
                print("Left edge", n)
                # Divide amongst two intervals
                result += n / 2
        elif z == right:
            if idx == len(occurrences) - 1:
                # Take all, as it's the right edge
                result += n
            else:
                print("Right edge", n)
                # Divide amongst two intervals
                result += n / 2

    return result


def get_phi(x):
    return round((1 / math.sqrt(2 * math.pi)) * math.e ** (- x ** 2 / 2), 4)


def get_laplas(x):
    if x == "-∞":
        return -0.5
    elif x == "+∞":
        return 0.5
    else:
        return round((1 / math.sqrt(2 * math.pi)) * integrate.quad(lambda x: math.e ** ((-x ** 2) / 2), 0, x)[0], 4)


def get_help_data_zi(equally_distributed, xb, sigma_b, h):
    result = []
    n = get_size_of_selection(equally_distributed)

    for idx, z in enumerate(equally_distributed):
        ui = round((z - xb) / xb, 2)
        phi = get_phi(ui)
        row = [idx + 1, z, ui, phi, round(((n * h) / sigma_b) * phi, 1)]

        result.append(row)

    return result


def get_help_data_ni(equally_distributed, xb, sigma_b, h):
    result = []
    n = get_size_of_selection(equally_distributed)
    sum_ni = 0
    x_2_obs = 0

    for idx, z in enumerate(equally_distributed):
        ui = round((z - xb) / xb, 2)
        phi = get_phi(ui)
        ni_dash = round(((n * h) / sigma_b) * phi, 1)
        ni = equally_distributed[z]
        sum_ni += ni
        last = round(((ni - ni_dash) ** 2) / ni_dash, 1)
        x_2_obs += last
        row = [idx + 1, ni, ni_dash, round(ni - ni_dash, 1), round((ni - ni_dash) ** 2, 2), last]

        result.append(row)

    result.append([
        "Σ", sum_ni, sum_ni, "", "", f"x^2сп = {x_2_obs}"
    ])

    return result


def task_one():
    arr = sorted([78, 64, 44, 73, 58, 88, 56, 68, 81, 52, 41, 65, 54, 90, 40, 56, 39, 60, 66, 58, 75,
                  60, 37, 78, 52, 59, 88, 80, 72, 69, 53, 57, 40, 62, 37, 62, 57, 58, 38, 46, 74, 44, 76, 36,
                  42, 80, 57, 45, 47, 88, 67, 87, 56, 68, 73, 72, 92, 68, 59, 71, 44, 76, 36, 49, 45, 38, 76,
                  66, 60, 78, 77, 42, 87, 60, 43, 36, 48, 64, 46, 59, 59, 77, 54, 79, 53, 92, 59, 53, 67, 82,
                  89, 76, 65, 89, 89, 75, 92, 72, 49, 59])

    occurrences = find_occurrences(arr)
    print(occurrences)

    h = 7
    start = arr[0]

    r = arr[-1] - arr[0]

    equally_distributed = {}

    for idx in range(int(r / h)):
        left = start + idx * h
        right = start + idx * h + h
        print(left, right)
        equally_distributed[left + h / 2] = get_n_within_interval(occurrences, left, right)

    print(equally_distributed)

    print(get_size_of_selection(equally_distributed))

    fig, ax = plt.subplots(1, 1)
    data = [list(equally_distributed.keys()), list(equally_distributed.values())]
    ax.axis('tight')
    ax.axis('off')
    ax.table(cellText=data, loc="center", rowLabels=["zi", "ni"])
    plt.show()

    xb = get_xb(equally_distributed)
    db = get_db(equally_distributed)
    sigma_b = math.sqrt(db)

    print(f"xb = {xb}")
    print(f"db = {db}")
    print(f"sigma_b = {sigma_b}")

    fig, ax = plt.subplots()
    data = get_help_data_zi(equally_distributed, xb, sigma_b, h)
    ax.axis('tight')
    ax.axis('off')
    n = get_size_of_selection(equally_distributed)
    ax.table(cellText=data, loc="center", cellLoc="center",
             colLabels=["i", "zi", r'ui = $\dfrac{{{}}}{{{}}}$'.format("zi - xb", "σb"), "φ(ui)",
                        f"ni' = {round(((n * h) / sigma_b), 1)} * φ(ui)"])
    plt.show()

    fig, ax = plt.subplots()
    data = get_help_data_ni(equally_distributed, xb, sigma_b, h)
    ax.axis('tight')
    ax.axis('off')
    ax.table(cellText=data, loc="center", cellLoc="center",
             colLabels=["i", "ni", "ni'", "ni - ni'", "(ni - ni')^2",
                        r'$\dfrac{{{}}}{{{}}}$'.format("(ni - ni')^2", "ni'")])

    plt.show()

    k = len(equally_distributed) - 3
    print(f"k = {k}")
    x_2_cr = 11.1  # (0.05, 5), з таблиці критичний розподілень x^2


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


def task_two():
    arr = [6, 32, 45, 14, 48, 34, 34, 2, 29, 11, 38, 8, 33, 30, 18, 37, 3, 8, 4, 49, 47, 24, 36, 1,
           11, 15, 3, 34, 45, 43, 35, 50, 24, 29, 14, 21, 12, 48, 23, 41, 9, 10, 49, 41, 39, 17, 27,
           42, 24, 31, 41, 20, 4, 26, 21, 14, 40, 24, 47, 35, 16, 32, 35, 40, 11, 49, 10, 23, 46, 33,
           13, 5, 42, 12, 45, 31, 28, 22, 23, 2, 2, 13, 22, 5, 38, 42, 19, 28, 15, 16, 13, 31, 47, 48,
           20, 8, 46, 30, 30, 42, 12, 42, 46, 3, 3, 41, 34, 31, 12, 6, 32, 13, 18, 3, 18, 6, 45, 37, 34,
           10, 3, 46, 40, 50, 43, 10, 7, 39, 39, 36, 31, 50, 28, 26, 3, 30, 16, 36, 11, 28, 41, 42, 41,
           9, 45, 9, 15, 39, 45, 48, 48, 47, 44, 38, 46, 37, 47, 2, 25, 35, 37, 5, 35, 14, 31, 37, 44,
           47, 22, 5, 24, 13, 46, 15, 22, 40, 23, 36, 29, 17, 34, 27, 14, 27, 14, 9, 13, 11, 11, 38,
           46, 48, 42, 30, 12, 23, 16, 6, 20, 38]

    arr = sorted(arr)
    occurrences = find_occurrences(arr)

    # 1. Інтервальний статистичний розподіл
    k = round(1 + 3.322 * math.log10(len(arr)))
    h = (arr[-1] - arr[0]) / k
    print(k, h)
    start = arr[-1] - k * h
    interval_occurrences = []
    intervals = []
    print(f"k = {k}")
    print(f"h = {h}")
    for i in range(k):
        result = 0
        left = start + i * h
        right = left + h
        print(left, right)
        intervals.append(f"{round(left, 2)}\n-\n{round(right, 2)}")
        for z in occurrences:
            if left < z < right:
                # Inside the range
                result += occurrences[z]
            elif z == left:
                # Left edge
                print("Left edge")
                # Take all
                result += occurrences[z]
            elif z == right:
                # Right edge
                print("Right edge")
                if i == (k - 1):
                    # End of array, take all
                    result += occurrences[z]

        interval_occurrences.append(result)

    fig, ax = plt.subplots(1, 1)
    data = [intervals, interval_occurrences]
    ax.axis('tight')
    ax.axis('off')
    table = ax.table(cellText=data, loc="center", rowLabels=[f"Інтервали,\nh={round(h, 2)}", "ni"])
    table.scale(1, 4)
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
    x_2_cr = 14.3  # Знайшов с таблиці x^2(0.025, 6)


def main():
    task_one()
    task_two()


if __name__ == '__main__':
    main()
