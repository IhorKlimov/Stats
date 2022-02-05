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


def task_one():
    occurrences = {
        6: 1,
        7: 3,
        8: 6,
        9: 8,
        10: 6,
        11: 6,
        12: 5,
        13: 3,
        14: 2
    }
    alpha = 0.001
    a = 8

    n = get_size_of_selection(occurrences)
    xb = get_xb(occurrences)
    print(f"xb = {xb}")
    s = math.sqrt(get_s2(occurrences))
    print(f"s = {s}")
    t_observed = ((xb - a) / s) * math.sqrt(n)
    print(f"t_obs = {t_observed}")
    k = n - 1
    print(f"k = {k}")
    t_crt = 2.43  # Знайшов з таблиці Стьюдента
    print(f"Theory is correct = {t_observed > (-t_crt)}")


def task_two():
    occurrences = {
        3: 2,
        3.5: 6,
        3.8: 9,
        4.4: 7,
        4.5: 1
    }

    alpha = 0.05
    a = 0.1
    n = get_size_of_selection(occurrences)
    print(f"n = {n}")

    s2 = get_s2(occurrences)
    print(f"s^2 = {s2}")

    k = n - 1
    x_2_obs = (k * s2) / a
    print(f"x^2obs = {x_2_obs}")

    f_z_a = (1 - 2 * alpha) / 2
    print(f"f_z_a = {f_z_a}")
    za = 1.65  # З таблиці Лапласа

    x_2_crt = k * (1 - (2 / (9 * k)) + za * math.sqrt((2 / (9 * k)))) ** 3
    print(f"x^2crt = {x_2_crt}")
    print(f"Theory is correct = {x_2_obs < x_2_crt}")


def main():
    task_one()
    task_two()


if __name__ == '__main__':
    main()
