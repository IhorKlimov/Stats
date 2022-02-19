def sum_of_elements(arr):
    result = 0

    for n in arr:
        result += n

    return result


def sum_of_elements_vertical(arr, idx):
    result = 0

    for row in arr:
        result += row[idx]

    return result


def avg(arr):
    return round(sum_of_elements(arr) / len(arr), 3)


def avg_vertical(arr, idx):
    return round(sum_of_elements_vertical(arr, idx) / len(arr), 3)


def get_s2_act_a(averages, x_total, m, n, k):
    sum_j = 0

    for j in range(k):
        print(f"get_s2_act_a -> ({averages[j][-1]} - {x_total}) ** 2")
        sum_j += (averages[j][-1] - x_total) ** 2

    print("sum check", sum_j)

    return round((m * n) / (k - 1) * sum_j, 6)


def get_s2_act_b(averages, x_total, m, n, k):
    sum_i = 0

    for i in range(n):
        print(f"get_s2_act_b -> ({averages[-1][i]} - {x_total}) ** 2")
        sum_i += (averages[-1][i] - x_total) ** 2

    return round((m * k) / (n - 1) * sum_i, 6)


def get_s2_common(averages, x_total, m, n, k):
    sum_common = 0

    for i in range(n):
        for j in range(k):
            print(f"get_s2_common -> ({averages[i][j]} - {averages[i][-1]} - {averages[-1][j]} + {x_total}) ** 2")
            sum_common += (averages[i][j] - averages[i][-1] - averages[-1][j] + x_total) ** 2

    return round(m / ((k - 1) * (n - 1)) * sum_common, 6)


def get_s2_remainder(input, averages, x_total, m, n, k):
    sum_remainder = 0

    for i in range(n):
        for j in range(k):
            for r in range(m):
                # print(f"get_s2_remainder -> ({input[i][j][r]} - {averages[i][j]}) ** 2")
                sum_remainder += (input[i][j][r] - averages[i][j]) ** 2

    return round(1 / ((n * k) * (m - 1)) * sum_remainder, 6)


def task_one():
    alpha = 0.05
    input = [
        [
            [6, 9, 12, 5, 7, 8, 8, 9],
            [5, 6, 6, 8, 11, 7, 9, 8],
            [10, 9, 8, 8, 10, 9, 7, 6]
        ],
        [
            [6, 9, 8, 11, 8, 7, 9, 9],
            [7, 8, 7, 12, 9, 9, 6, 8],
            [8, 7, 8, 8, 12, 9, 6, 5]
        ],
        [
            [7, 9, 12, 5, 9, 8, 7, 6],
            [9, 6, 5, 13, 8, 9, 7, 8],
            [8, 8, 12, 7, 6, 9, 9, 5]
        ]
    ]

    averages = []
    for a in input:
        res = []
        for b in a:
            res.append(avg(b))

        averages.append(res)

    for a in averages:
        a.append(avg(a))

    row = []
    for idx in range(len(averages[0])):
        row.append(avg_vertical(averages, idx))

    averages.append(row)

    print("Table:")
    for a in averages:
        print(a)

    n = len(input)
    m = len(input[0][0])
    k = len(input[0])

    print(f"n = {n}")
    print(f"m = {m}")
    print(f"k = {k}")

    x_total = averages[-1][-1]
    print(f"x_total = {x_total}")

    s2_act_a = get_s2_act_a(averages, x_total, m, n, k)
    s2_act_b = get_s2_act_b(averages, x_total, m, n, k)
    s2_common = get_s2_common(averages, x_total, m, n, k)
    s2_remainder = get_s2_remainder(input, averages, x_total, m, n, k)
    print(f"s2_act_a = {s2_act_a}")
    print(f"s2_act_b = {s2_act_b}")
    print(f"s2_common = {s2_common}")
    print(f"s2_remainder = {s2_remainder}")

    f_obs_a = round(s2_act_a / s2_remainder, 2)
    f_obs_b = round(s2_act_b / s2_remainder, 2)
    f_obs_total = round(s2_common / s2_remainder, 2)
    print(f"f_obs_a = {f_obs_a}")
    print(f"f_obs_b = {f_obs_b}")
    print(f"f_obs_total = {f_obs_total}")

    k1 = n - 1
    k2 = n * k * (m - 1)
    print(f"k1 = {k1}")
    print(f"k2 = {k2}")

    fcra = 3.142808517  # Знайшов з таблиці Фишера - Снедекора
    fcrb = fcra
    print(f"Fcra({alpha}, {k1}, {k2}) = {fcra}")
    print(f"Fcrb({alpha}, {k1}, {k2}) = {fcrb}")
    print(f"f_obs_a > fcra {f_obs_a > fcra}")
    print(f"f_obs_b > fcrb {f_obs_b > fcrb}")

    k1 = (k - 1) * (n - 1)
    k2 = n * k * (m - 1)
    fcr_common = 2.517670458  # Знайшов з таблиці Фишера - Снедекора
    print(f"Fcrcommon({alpha}, {k1}, {k2}) = {fcr_common}")
    print(f"f_obs_total > fcr_common {f_obs_total > fcr_common}")


if __name__ == '__main__':
    task_one()
