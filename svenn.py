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



x0 = 3.5
svenn_output = svenn_method(func, x0, 0.1)
a, c = svenn_output[0], svenn_output[1]
print(f"Відрізок, що містить точку мінімуму: [{round(a, 3)}, {round(svenn_output[2], 3)}, {round(c, 3)}]")
print(f"x_m = {round(svenn_output[2], 3)}")
print(f"f(x_m) = {round(svenn_output[3], 3)}")
