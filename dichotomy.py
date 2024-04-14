lb = 2
rb = 2.8

svenn_x_m_val = 2.4
svenn_x_m_func = -6.24

epsilon = 0.2


def func(x):
    return (x ** 2) - 5 * x

def dichotomy(left_bound, right_bound):
    i = 0
    x_m = svenn_x_m_val
    f_x_m = svenn_x_m_func
    while True:
        i += 1
        print(f"Ітерація: {i}")

        L = right_bound - left_bound

        print(left_bound, x_m, round(right_bound, 3))
        print(func(left_bound), func(x_m), round(func(right_bound), 3))

        if L <= epsilon:
            return round(left_bound, 3), round(right_bound, 3)


        if x_m != svenn_x_m_val:
            f_x_m = func(x_m)

        if func(right_bound) >= f_x_m >= func(left_bound):
            right_bound = x_m
            x_m = (left_bound + right_bound) / 2
            continue
        elif func(left_bound) >= f_x_m >= func(right_bound):
            left_bound = x_m
            x_m = (left_bound + right_bound) / 2
            continue

        left_bound = (left_bound + x_m) / 2
        right_bound = (right_bound + x_m) / 2



print(f"Відповідь: ", dichotomy(lb, rb))




# def dichotomy(left_bound, right_bound):
#     x_m = (left_bound + right_bound) / 2
#     f_x_m = func(x_m)
#
#     L = right_bound - left_bound
#
#     if L <= epsilon:
#         return round(left_bound, 3), round(right_bound, 3)
#
#     x_1 = (left_bound + x_m) / 2
#     x_2 = (right_bound + x_m) / 2
#
#     if func(x_1) > f_x_m and func(x_2) > f_x_m:
#         print(1)
#         return dichotomy(x_1, x_2)
#     elif func(x_1) <= f_x_m:
#         print(2)
#         return dichotomy(x_1, x_m)
#     elif func(x_2) <= f_x_m:
#         print(3)
#         return dichotomy(x_m, x_2)


# ???????????????????????????
