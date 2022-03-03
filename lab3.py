import math


def task_one():
    occurrences = {
        5: 3,
        11: 4,
        13: 3,
        17: 7,
        20: 3
    }

    n = 0
    for ni in occurrences.values():
        n += ni

    sum_of_elements = 0
    for z in occurrences:
        sum_of_elements += z * occurrences[z]
    xb = 1 / n * sum_of_elements
    print(f"xb = 1 / {n} * {sum_of_elements} = {xb}")

    db_sum = 0
    for z in occurrences:
        db_sum += (z - xb) ** 2 * occurrences[z]
    db = 1 / n * db_sum
    print(f"Db = 1 / {n} * {db_sum} = {db}")

    s2 = n / (n - 1) * db
    print(f"s2 = {n} / ({n} - 1) * {db} = {s2}")

    s = math.sqrt(s2)
    print(f"s = {s}")

    ty = 2.093  # Знайшов з таблиці значень ty, по y = 0.95, n = 20
    left = xb - (s * ty) / math.sqrt(n)
    right = xb + (s * ty) / math.sqrt(n)
    print(f"left = {xb} - ({s} * {ty}) / {math.sqrt(n)} = {left}")
    print(f"right = {xb} + ({s} * {ty}) / {math.sqrt(n)} = {right}")

    print(f"Task 1. {left} < a < {right}")


def task_two():
    h = 2  # Розмір інтервалів
    k = 7
    start = 4
    interval_occurrences = [8, 15, 24, 20, 19, 10, 4]
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

    n = 0
    for ni in occurrences.values():
        n += ni

    print(f"n = {n}")

    sum_of_elements = 0
    for z in occurrences:
        sum_of_elements += z * occurrences[z]
    xb = 1 / n * sum_of_elements
    print(f"xb = 1 / {n} * {sum_of_elements} = {xb}")

    sigma = 8  # С Завдання
    y = 0.9545  # С Завдання
    f_of_t = y / 2
    print(f"F(t) = {f_of_t}")  # F(t) = 0.47725
    t = 2  # Знайшов 0.47725 у Таблиці Лапласа

    left = xb - (sigma * t) / math.sqrt(n)
    right = xb + (sigma * t) / math.sqrt(n)

    print(f"left = {xb} - ({sigma} * {t}) / {math.sqrt(n)} = {left}")
    print(f"right = {xb} + ({sigma} * {t}) / {math.sqrt(n)} = {right}")
    print(f"Task 2. {left} < a < {right}")


def task_three():
    occurrences = {
        1: 2,
        2: 3,
        3: 5,
        4: 4,
        5: 1
    }
    y = 0.99  # С завдання

    n = 0
    for ni in occurrences.values():
        n += ni

    print(f"n = {n}")
    q = 0.73  # Знайшов з Таблиці значень q, по n = 15, y = 0.99

    sum_of_elements = 0
    for z in occurrences:
        sum_of_elements += z * occurrences[z]
    xb = 1 / n * sum_of_elements
    print(f"xb = 1 / {n} * {sum_of_elements} = {xb}")

    db_sum = 0
    for z in occurrences:
        db_sum += (z - xb) ** 2 * occurrences[z]
    db = 1 / n * db_sum
    print(f"Db = 1 / {n} * {db_sum} = {db}")

    s2 = n / (n - 1) * db
    print(f"s2 = {n} / ({n} - 1) * {db} = {s2}")

    s = math.sqrt(s2)
    print(f"s = {s}")

    if q > 1:
        left = 0
        right = s * (1 + q)
        print(f"left = {left}")
        print(f"right = {s} * (1 + {q}) = {right}")
    else:
        left = s * (1 - q)
        right = s * (1 + q)
        print(f"left = {s} * (1 - {q}) = {left}")
        print(f"right = {s} * (1 + {q}) = {right}")

    print(f"Task 3. {left} < a < {right}")


def main():
    task_one()
    task_two()
    task_three()


if __name__ == '__main__':
    main()
