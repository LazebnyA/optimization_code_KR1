lb = 2
rb = 2.8

epsilon = 0.2


def func(x):
    return x**2 - 5*x


def golden_section(left_bound, right_bound):

    a = left_bound
    b = right_bound

    i = 0

    while True:
        i += 1
        print(f"Ітерація: {i}")

        L = b - a

        x1 = a + 0.382 * L
        x2 = a + 0.618 * L

        print("L: ", L)
        print(x1, x2)

        if abs(L) < epsilon:
            print("Interval:", round(x1, 3), round(x2, 3))
            return round(a, 3), round(b, 3)

        if func(x1) > func(x2):
            a = x1
            x1 = x2
            x2 = a + 0.618 * L
        else:
            b = x2
            x2 = x1
            x1 = a + 0.382 * L


print(golden_section(lb, rb))
