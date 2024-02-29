epsilon = 0.2


def func(x):
    return (x ** 2) - 5 * x


def svenn_method(func, x0, h):
    a, b = x0, x0 + h
    fa, fb = func(a), func(b)

    if fa < fb:
        h = -h
        a, b = x0, x0 + h

    c = b + 2 * h
    fc = func(c)

    while True:
        h *= 2
        b, fb = c, fc
        c = b + 2 * h
        fc = func(c)
        if fc > fb:
            break

    if h < 0:
        left_bound = (b + c) / 2
        right_bound = b - h
    else:
        left_bound = b - h
        right_bound = (b + c) / 2

    return left_bound, right_bound, b, fb


def check_error(DSK_min, svenn_min):
    if abs(func(svenn_min) - func(DSK_min)) <= epsilon and abs(svenn_min - DSK_min) <= epsilon:
        print(abs(func(svenn_min) - func(DSK_min)))
        print(abs(svenn_min - DSK_min) < epsilon)
        return True
    return False


result = svenn_method(func, 3.5, 0.1)
lb, rb = result[0], result[1]
print(f"Ітерація: 1")
# print(f"Interval containing the minimum point: [{round(lb, 2)}, {round(result[2], 2)}, {round(rb, 2)}]")
# print(f"x_m = {round(result[2], 2)}")
# print(f"f(x_m) = {result[3]}")



x_1 = lb
x_2 = result[2]
x_3 = rb

delta_x = x_3 - x_2
x_min = x_2 + delta_x * (func(x_1) - func(x_3)) / (
        2 * (func(x_1) - 2 * func(x_2) + func(x_3)))

print(f"x_min = {round(x_min, 3)}, f({round(x_min, 3)}) = {round(func(x_min), 3)}")

print(f"x_1 = {round(x_1, 3)}, x_2 = {round(x_2, 3)}, x_3 = {round(x_3, 3)}, x_* = {round(x_min, 3)}")

print("_"*50)

prev_min = x_2

i = 1
while True:
    if check_error(x_min, prev_min):
        break

    i += 1
    print(f"Ітерація: {i}")


    if x_min > prev_min:
        x_1 = x_2
        x_2 = x_min
    elif x_min < prev_min:
        x_3 = x_2
        x_2 = x_min

    a_1 = (func(x_2) - func(x_1)) / (x_2 - x_1)
    a_2 = (((func(x_3) - func(x_1)) / (x_3 - x_1)) -
           ((func(x_2) - func(x_1)) / (x_2 - x_1))) / (x_3 - x_2)

    prev_min = x_min
    x_min = ((x_1 + x_2) / 2) - (a_1 / (2 * a_2))

    print(f"x_min = {round(x_min, 3)}, f({round(x_min, 3)}) = {round(func(x_min), 3)}")

    print(f"x_1 = {round(x_1, 3)}, x_2 = {round(x_2, 3)}, x_3 = {round(x_3, 3)}, x_* = {round(x_min, 3)}")

    print("_" * 50)





print(x_min, func(x_min))
