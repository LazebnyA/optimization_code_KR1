lb = 2.4
rb = 3.2

epsilon = 0.2


def func(x):
    return (x ** 2) - (5 * x)


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

        if abs(func(x1) - func(x2)) < epsilon:
            print("Interval:", round(x1, 3), round(x2, 3))
            return round(x1, 3), round(x2, 3)

        if func(x1) < func(x2):
            b = x2
        else:
            a = x1





print(golden_section(lb, rb))

# def get_min(left_bound=lb, right_bound=rb, L=rb-lb):
#
#     x_1 = left_bound + 0.382 * L
#     x_2 = left_bound + 0.618 * L
#
#     if func(x_2) > func(x_1):
#         L = x_2 - left_bound
#         print(f"Межі на відповідь: {round(left_bound, 2)}, {round(x_2, 2)}")
#
#         if L <= epsilon:
#             return left_bound, right_bound
#
#         print(left_bound + 0.382 * L, x_1)
#         return get_min(left_bound + 0.382 * L, x_1, L)
#     elif func(x_1) > func(x_2):
#         L = right_bound - x_1
#         print(f"Межі на відповідь: {round(x_1, 2)}, {round(right_bound, 2)}")
#         if L <= epsilon:
#             return left_bound, right_bound
#
#         print(x_2, left_bound + 0.618 * L)
#         return get_min(x_2, left_bound + 0.618 * L, L)
#
#     return get_min(x_1, x_2, L)




# ???????????????????????????
