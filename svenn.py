def func(x):
    return (x ** 2) - 5 * x


def half_sum(x, y):
    return (x + y) / 2


def get_result(b, h):
    if h < 0:
        left_bound = b + h
        right_bound = b - h
    else:
        left_bound = b - h
        right_bound = b + h

    print(left_bound, func(left_bound), right_bound, func(right_bound))
    return left_bound, right_bound


def svenn_method(func, x0, h):
    a, b = x0, x0 + h
    fa, fb = func(a), func(b)

    print(a, fa, b, fb)

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

        print(b, fb, c, fc)

        if fc > fb and func(half_sum(b, c)) > fb:
            return get_result(b, h)
        elif fc > fb >= func(half_sum(b, c)):
            b = half_sum(b, c)
            print(f"b = {b}, h = {h}")
            return get_result(b, h)


x0 = 3.5
svenn_output = svenn_method(func, x0, 0.1)
a, c = svenn_output[0], svenn_output[1]
print(f"Відрізок, що містить точку мінімуму: [{round(a, 3)}, {round(c, 3)}]")
