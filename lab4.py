import math

from matplotlib import pyplot as plt


def task_one():
    coordinates = {
        1: -7,
        3: -3,
        4: 2,
        7: 8,
        10: 18,
        12: 24,
        15: 30,
        18: 44,
        20: 48,
        25: 55
    }

    # Зображення координат
    fig, ax = plt.subplots()
    ax.spines[["left", "bottom"]].set_position(("data", 0))
    ax.spines[["top", "right"]].set_visible(False)
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    ax.scatter(list(coordinates.keys()), list(coordinates.values()))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

    fig, ax = plt.subplots(1, 1)
    data = []

    for idx, x in enumerate(coordinates):
        y = coordinates[x]
        data.append([idx + 1, x, y, x ** 2, x * y])

    sum_x = 0
    sum_y = 0
    sum_x_squared = 0
    sum_x_times_y = 0
    for row in data:
        sum_x += row[1]
        sum_y += row[2]
        sum_x_squared += row[3]
        sum_x_times_y += row[4]

    data.append(["Σ", sum_x, sum_y, sum_x_squared, sum_x_times_y])

    ax.axis('tight')
    ax.axis('off')
    ax.table(cellText=data, loc="center", cellLoc="center", colLabels=["№", "xi", "yi", "xi^2", "xi*yi"])
    plt.show()


def sum_of_elements(arr):
    result = 0

    for n in arr:
        result += n

    return result


def sum_of_elements_2d(idx, arr):
    result = 0

    for row in arr:
        result += row[idx]

    return result


def to_display_data(x, y, data):
    result = []

    r = ["y \ x"]
    for n in x:
        r.append(n)

    r.append("Σ")
    result.append(r)

    for idx, row in enumerate(data):
        r = [y[idx]]

        for n in row:
            if n == 0:
                r.append("-")
            else:
                r.append(n)

        r.append(sum_of_elements(row))
        result.append(r)

    sums = ["Σ"]
    result.append(sums)
    total_sum = 0
    for n in range(len(data[0])):
        s = sum_of_elements_2d(n, data)
        total_sum += s
        sums.append(s)

    sums.append(total_sum)

    return result


def convert_to_conditional(arr, c, h):
    converted = []
    for n in arr:
        converted.append(int((n - c) / h))

    return converted


def task_two():
    x = [2, 4, 6, 8, 10, 12, 14, 16]
    y = [3, 7, 11, 15, 19]
    data = [
        [7, 11, 0, 0, 0, 0, 0, 0],
        [5, 4, 10, 0, 0, 0, 0, 0],
        [4, 3, 6, 14, 5, 0, 0, 0],
        [0, 0, 0, 4, 3, 10, 3, 3],
        [0, 0, 0, 0, 0, 3, 4, 1]
    ]

    fig, ax = plt.subplots(1, 1)
    ax.axis('tight')
    ax.axis('off')
    ax.table(cellText=to_display_data(x, y, data), loc="center", cellLoc="center")
    plt.show()

    h1 = x[1] - x[0]
    h2 = y[1] - y[0]
    center_x = math.ceil(len(x) / 2) - 1
    c1 = x[center_x]
    center_y = math.ceil(len(y) / 2) - 1
    c2 = y[center_y]
    print(f"h1 = {h1}")
    print(f"h2 = {h2}")
    print(f"C1 = {c1}")
    print(f"C2 = {c2}")

    converted_x = convert_to_conditional(x, c1, h1)
    converted_y = convert_to_conditional(y, c2, h2)

    fig, ax = plt.subplots(1, 1)
    ax.axis('tight')
    ax.axis('off')
    ax.table(cellText=to_display_data(converted_x, converted_y, data), loc="center", cellLoc="center")
    plt.show()

    total_num_of_elements = to_display_data(converted_x, converted_y, data)[-1][-1]

    sum_of_x = 0
    for idx, x in enumerate(converted_x):
        sum_of_x += x * sum_of_elements_2d(idx, data)

    ub = sum_of_x / total_num_of_elements

    sum_of_y = 0
    for idx, y in enumerate(converted_y):
        print(f"check {y} {sum_of_elements(data[idx])}")
        sum_of_y += y * sum_of_elements(data[idx])

    vb = sum_of_y / total_num_of_elements

    print(f"ub = {ub}")
    print(f"vb = {vb}")

    sum_2_of_x = 0
    for idx, x in enumerate(converted_x):
        sum_2_of_x += x ** 2 * sum_of_elements_2d(idx, data)

    u_2_b = sum_2_of_x / total_num_of_elements

    sum_2_of_y = 0
    for idx, y in enumerate(converted_y):
        sum_2_of_y += y ** 2 * sum_of_elements(data[idx])

    v_2_b = sum_2_of_y / total_num_of_elements

    print(f"u^2b = {u_2_b}")
    print(f"v^2b = {v_2_b}")

    sigma_u = math.sqrt(u_2_b - ub ** 2)
    sigma_v = math.sqrt(v_2_b - vb ** 2)

    print(f"sigma u = {sigma_u}")
    print(f"sigma v = {sigma_v}")

    sum_x_y_n = 0
    for y_idx, row in enumerate(data):
        for x_idx, n in enumerate(row):
            sum_x_y_n += converted_x[x_idx] * converted_y[y_idx] * n

    print(f"sum of x_y_n = {sum_x_y_n}")

    rb = (sum_x_y_n - total_num_of_elements * ub * vb) / (total_num_of_elements * sigma_u * sigma_v)
    print(f"rb = {rb}")

    xb = ub * h1 + c1
    yb = vb * h2 + c2
    sigma_x = sigma_u * h1
    sigma_y = sigma_v * h2

    print(f"xb = {xb}")
    print(f"yb = {yb}")
    print(f"sigma x = {sigma_x}")
    print(f"sigma y = {sigma_y}")

    print(f"y - {yb} = {rb} * {sigma_y} / {sigma_x} * (x - {xb})")

    print(f"y = {rb * (sigma_y / sigma_x)}x + {yb + (rb * (sigma_y / sigma_x) * -xb)}")



def main():
    task_one()
    task_two()


if __name__ == '__main__':
    main()
