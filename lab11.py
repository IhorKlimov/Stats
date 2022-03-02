import math
import tkinter.tix

from matplotlib import pyplot as plt


def get_p(la, k, t):
    return ((la * t) ** k) / math.factorial(k) * (math.e ** (-la * t))


def task_one():
    la = 3
    t = 2

    four = get_p(la, 4, t)
    less_than_four = get_p(la, 0, t) + get_p(la, 1, t) + get_p(la, 2, t)
    more_or_equals_to_four = 0
    for k in range(4, 100_000_000):
        p = get_p(la, k, t)
        print(k, p)
        if p == 0:
            break

        more_or_equals_to_four += p

    print(f"Probability of 4 = {four}")
    print(f"Probability of < 4 = {less_than_four}")
    print(f"Probability of >= 4 = {more_or_equals_to_four}")


def apply_xi_function(t, n):
    return t ** 2 * n + 5


def apply_xi_function_2(t, n):
    return t * n - 1


def task_two():
    input = {
        -1: 0.2,
        0: 0.1,
        1: 0.4,
        2: 0.3
    }

    t = 3
    data = [list(map(lambda n: apply_xi_function(t, n), input.keys())), list(input.values())]

    fig, ax = plt.subplots()
    ax.axis('tight')
    ax.axis('off')
    ax.table(cellText=data, loc="center", cellLoc="center", rowLabels=["n", "P"])
    plt.show()


def task_three():
    a = 4
    sigma = 3
    t = 2


def task_four():



if __name__ == '__main__':
    task_one()
    task_two()
    task_three()
    task_four()
