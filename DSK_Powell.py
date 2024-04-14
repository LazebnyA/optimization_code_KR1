lb = 2
rb = 2.8

svenn_x_m_val = 2.4
svenn_x_m_func = -6.24

epsilon = 0.2


def func(x):
    return (x ** 2) - 5 * x

def check_error(DSK_min, svenn_min):
    if abs(func(svenn_min) - func(DSK_min)) <= epsilon and abs(svenn_min - DSK_min) <= epsilon:
        print(abs(func(svenn_min) - func(DSK_min)))
        print(abs(svenn_min - DSK_min) < epsilon)
        return True
    return False


print(f"Ітерація: 1")
# print(f"Interval containing the minimum point: [{round(lb, 2)}, {round(result[2], 2)}, {round(rb, 2)}]")
# print(f"x_m = {round(result[2], 2)}")
# print(f"f(x_m) = {result[3]}")



x_1 = lb
x_2 = svenn_x_m_val
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
