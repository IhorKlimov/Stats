import math

import matplotlib.pyplot as plt


def find_occurrences(arr):
    result = {}
    for n in arr:
        if n in result:
            result[n] = result[n] + 1
        else:
            result[n] = 1

    return dict(sorted(result.items()))


def main():
    arr = [1, 9, 7, 7, 4, 13, 1, 7, 11, 7,
           4, 7, 1, 11, 11, 7, 11, 4, 1, 7,
           7, 9, 7, 9, 4, 1, 11, 1, 13, 4,
           9, 13, 1, 11, 7, 13, 9, 11, 7, 11,
           1, 4, 11, 4, 9, 4, 7, 1, 9, 13]

    arr = sorted(arr)

    occurrences = find_occurrences(arr)
    zi = list(occurrences.keys())
    ni = list(occurrences.values())

    # 1. Дискретний статистичний розподіл
    fig, ax = plt.subplots(1, 1)
    data = [zi, ni]
    ax.axis('tight')
    ax.axis('off')
    ax.table(cellText=data, loc="center", rowLabels=[r"$z_i$", r"$n_i$"])
    plt.show()

    # 2. Полігон
    fig, ax = plt.subplots()
    ax.spines[["left", "bottom"]].set_position(("data", 0))
    ax.spines[["top", "right"]].set_visible(False)
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    ax.plot(zi, ni, marker='o')
    plt.ylabel(r"$n_i$")
    plt.xlabel(r"$z_i$")
    plt.xticks(zi)
    plt.yticks(ni)
    ax.vlines(zi, 0, ni, linestyle="dashed", linewidth=1.0)
    ax.hlines(ni, 0, zi, linestyle="dashed", linewidth=1.0)
    plt.show()

    # 3. Гістограма частот
    fig, ax = plt.subplots()
    ax.spines[["left", "bottom"]].set_position(("data", 0))
    ax.spines[["top", "right"]].set_visible(False)
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    ax.bar(zi, ni, width=1.0, fill=False)
    plt.ylabel('ni')
    plt.xlabel('zi')
    plt.xticks(zi)
    plt.yticks(ni)
    ax.hlines(ni, 0, zi, linestyle="dashed", linewidth=1.0, colors="#000000", alpha=0.5)
    plt.show()

    # 4. Розподіл відносних частот
    fig, ax = plt.subplots()
    data = [zi, list(map(lambda x: r'$\dfrac{{{}}}{{{}}}$'.format(x, len(arr)), ni))]
    ax.axis('tight')
    ax.axis('off')
    t = ax.table(cellText=data, loc="center", rowLabels=[r"$z_i$", "vi"])
    t.scale(1, 2)
    plt.show()

    # 5. Емпірична функція розподілу. Зброблено за допомогою https://www.mathcha.io
    # 6. Графік емпіричної функція розподілу. Зроблено на бумазі

    # 7. Середнє вибіркове
    sum_of_elements = 0
    for z in occurrences:
        sum_of_elements += z * occurrences[z]

    xb = 1 / len(arr) * sum_of_elements
    print(f"xb = {xb}")

    # 8. Вибіркова дисперсія
    db_sum = 0
    for z in occurrences:
        db_sum += (z - xb) ** 2 * occurrences[z]

    db = 1 / len(arr) * db_sum
    print(f"Db = {db}")

    # 9. Виправлена вибіркова дисперсія
    s2 = len(arr) / (len(arr) - 1) * db
    print(f"s2 = {s2}")

    # 10. Розмах
    r = zi[-1] - zi[0]
    print(f"R = {r}")

    # 11. Коефіцієнт варіації
    v = math.sqrt(db) / xb * 100
    print(f"V = {v}%")

    # 12. Мода
    mo = None
    max_z = None
    for z in occurrences:
        if max_z is None or occurrences[z] > max_z:
            max_z = occurrences[z]
            mo = z

    print(f"mo = {mo}")

    # 13. Медіана
    k = int(len(arr) / 2) - 1
    print(f"k = {k}")
    if len(arr) % 2 == 0:
        me = (arr[k] + arr[k + 1]) / 2
    else:
        me = arr[k + 1]

    print(f"me = {me}")


if __name__ == '__main__':
    main()
