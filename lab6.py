import math


def get_size_of_selection(occurrences):
    n = 0
    for ni in occurrences.values():
        n += ni

    return n


def get_s2(occurrences):
    xb = get_xb(occurrences)
    n = get_size_of_selection(occurrences)
    db_sum = 0
    for z in occurrences:
        db_sum += (z - xb) ** 2 * occurrences[z]

    db = 1 / n * db_sum

    return n / (n - 1) * db


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


def task_one():
    occurrences_1 = {
        6.64: 4,
        6.7: 8,
        6.74: 12,
        6.78: 10,
        6.82: 6
    }

    occurrences_2 = {
        6.58: 8,
        6.6: 12,
        6.8: 15,
        7: 6,
        7.2: 4
    }

    a = 0.01
    d_1 = 50
    d_2 = 60
    n = get_size_of_selection(occurrences_1)
    m = get_size_of_selection(occurrences_2)

    xb = get_xb(occurrences_1)
    yb = get_xb(occurrences_2)
    print(f"xb = {xb}")
    print(f"yb = {yb}")

    z_obs = (xb - yb) / (math.sqrt(d_1 / n + d_2 / m))
    print(f"z_obs = {z_obs}")

    f_z_cr = (1 - 2 * a) / 2
    print(f"F(zcr) = {f_z_cr}")

    z_cr = 2.33  # Знайшов з Таблиці Лапласа
    print(f"Hypothesis is true = {z_obs < z_cr}")


def task_two():
    coordinates = [
        [25, 27],
        [20, 22],
        [26, 24],
        [22, 25],
        [24, 26],
        [24, 27],
        [28, 25],
        [21, 24],
        [25, 26]
    ]

    a = 0.05
    di = []
    for c in coordinates:
        di.append(c[0] - c[1])

    print(di)

    di_sum = 0
    for d in di:
        di_sum += d

    n = len(coordinates)
    db = di_sum / n
    print(f"db = {db}")

    sd_sum = 0
    for d in di:
        sd_sum += d ** 2

    print(f"sd_sum = {sd_sum}")

    sd = math.sqrt(
        (n / (n - 1)) * (sd_sum / n - (db ** 2))
    )
    print(f"sd = {sd}")

    t_obs = (db * math.sqrt(n)) / sd
    print(f"t obs = {t_obs}")

    t_cr = 2.25  # З таблиці Стьюдента
    print(f"Hypothesis is correct = {math.fabs(t_obs) < t_cr}")


def main():
    task_one()
    task_two()


if __name__ == '__main__':
    main()
