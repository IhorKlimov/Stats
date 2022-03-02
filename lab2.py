import math

from matplotlib import pyplot as plt


def find_occurrences(arr):
    result = {}
    for n in arr:
        if n in result:
            result[n] = result[n] + 1
        else:
            result[n] = 1

    return dict(sorted(result.items()))


def main():
    arr = [66, 59, 65, 42, 49, 42, 45, 65, 64, 60, 62, 52, 56, 72, 55, 60, 54, 58, 65, 69, 64, 73, 48,
           67, 41, 58, 41, 43, 44, 37, 62, 74, 60, 49, 38, 73, 55, 48, 59, 41, 73, 43, 57, 50, 37, 76,
           74, 56, 56, 61, 46, 41, 56, 59, 73, 61, 38, 78, 69, 46, 37, 52, 42, 61, 65, 45, 56, 41, 57,
           37, 47, 51, 45, 68, 66, 46, 66, 62, 67, 43, 45, 77, 49, 65, 57, 44, 48, 59, 44, 38, 70, 45,
           55, 76, 70, 41, 42, 48, 47, 64]

    arr = sorted(arr)
    occurrences = find_occurrences(arr)
    print(occurrences)

    # 1. Інтервальний статистичний розподіл
    k = round(1 + 3.322 * math.log10(len(arr)))
    h = (arr[-1] - arr[0]) / k
    print(k, h)
    start = arr[-1] - k * h
    interval_occurrences = []
    intervals = []
    for i in range(k):
        result = 0
        left = start + i * h
        right = left + h
        intervals.append(f"{left}\n-\n{right}")
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
    table = ax.table(cellText=data, loc="center", rowLabels=[f"Інтервали,\nh={h}", "ni"])
    table.scale(1, 4)
    plt.show()

    # 2. Гістограма частот
    zi = [start]
    for i in range(k):
        left = start + i * h
        right = left + h
        zi.append(right)

    print(zi, interval_occurrences)
    fig, ax = plt.subplots()
    ax.spines[["left", "bottom"]].set_position(("data", 0))
    ax.spines[["top", "right"]].set_visible(False)
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    ax.hist(arr, bins=k, fill=False)
    plt.ylabel('ni')
    plt.xlabel('xi')
    plt.xticks(zi)
    plt.yticks(interval_occurrences)
    ax.hlines(interval_occurrences, 0, zi[1:], linestyle="dashed", linewidth=1.0, colors="#000000", alpha=0.5)
    plt.show()

    # 3. Середнє вибіркове
    discrete_zi = []
    for i in range(len(zi) - 1):
        discrete_zi.append(zi[i] + h / 2)

    sum_of_elements = 0
    for z in range(len(discrete_zi)):
        sum_of_elements += discrete_zi[z] * interval_occurrences[z]

    xb = 1 / len(arr) * sum_of_elements
    print(f"xb = 1 / {len(arr)} * {sum_of_elements} = {xb}")

    # 4. Вибіркова дисперсія
    db_sum = 0
    for idx, z in enumerate(discrete_zi):
        db_sum += (z - xb) ** 2 * interval_occurrences[idx]
        print(idx, z)

    db = 1 / len(arr) * db_sum
    print(f"Db = 1 / {len(arr)} * {db_sum} = {db}")

    # 5. Виправлена вибіркова дисперсія
    s2 = len(arr) / (len(arr) - 1) * db
    print(f"s2 = {len(arr)} / ({len(arr)} - 1) * {db} = {s2}")

    # 6. Розмах
    r = zi[-1] - zi[0]
    print(f"R = {zi[-1]} - {zi[0]} = {r}")

    # 7. Коефіцієнт варіації
    v = math.sqrt(db) / xb * 100
    print(f"V = {math.sqrt(db)} / {xb} * 100 = {v}%")

    # 8. Мода
    interval_max_occurrence = None
    interval_max_occurrence_idx = None
    for idx, ni in enumerate(interval_occurrences):
        if interval_max_occurrence is None or ni > interval_max_occurrence:
            interval_max_occurrence = ni
            interval_max_occurrence_idx = idx

    print(interval_max_occurrence, interval_max_occurrence_idx)

    modal_interval = [start + h * interval_max_occurrence_idx, start + h + h * interval_max_occurrence_idx]

    nmo = interval_occurrences[interval_max_occurrence_idx]
    nmo_minus_one = 0
    if interval_max_occurrence_idx - 1 >= 0:
        nmo_minus_one = interval_occurrences[interval_max_occurrence_idx - 1]

    nmo_plus_one = 0
    if interval_max_occurrence_idx + 1 >= 0:
        nmo_plus_one = interval_occurrences[interval_max_occurrence_idx + 1]

    print(nmo, modal_interval[0], nmo_minus_one, nmo_plus_one)

    mo = modal_interval[0] + h * ((nmo - nmo_minus_one) / (2 * nmo - nmo_minus_one - nmo_plus_one))
    print(f"mo = {modal_interval[0]} + {h} * (({nmo} - {nmo_minus_one}) / (2 * {nmo} - {nmo_minus_one} - {nmo_plus_one})) = {mo}")

    # 9. Медіана
    half = len(arr) / 2
    median_interval_idx = None
    median_interval = None
    sum_of_preceding_elements = 0

    for n in range(k):
        left = start + n * h
        right = left + h
        print(f"check {left} {right}")
        if half >= left and (half < right or n == k - 1):
            median_interval_idx = n
            median_interval = [left, right]
            break
        else:
            sum_of_preceding_elements += interval_occurrences[n]

    me = median_interval[0] + h * (
            (len(arr) / 2 - sum_of_preceding_elements) / interval_occurrences[median_interval_idx])

    print(f"me = {median_interval[0]} + {h} * (({len(arr)} / 2 - {sum_of_preceding_elements}) / {interval_occurrences[median_interval_idx]}) = {me}")


if __name__ == '__main__':
    main()
