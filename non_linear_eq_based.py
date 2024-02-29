def func(x):
    return (x ** 2) + 5 / x


def first_derivative(x):
    return 2 * x - (5 / x ** 2)


def second_derivative(x):
    return (10 / (x ** 3)) + 2


def newton_raphson(x_0):
    x_i = x_0
    for i in range(3):
        print(f"Ітерація: {i+1}")

        print(
            f"x_{i} = {round(x_i, 3)}, f'({round(x_i, 3)}) = {round(first_derivative(x_i), 3)}, f''({round(x_i, 3)}) = {round(second_derivative(x_i), 3)}")
        print(f"|f'(x_{i})| = {abs(round(first_derivative(x_i), 3))}")
        x_i = x_i - (first_derivative(x_i) / second_derivative(x_i))
        print(f"x_{i + 1} = {round(x_i, 3)}")
        print("_" * 50)


def middle_point(lb, rb):
    for i in range(3):
        print(f"Ітерація: {i + 1}")

        x_middle = 0.5 * (lb + rb)
        gradient_x_middle = round(first_derivative(x_middle), 3)
        print(
            f"x_1 = {round(lb, 3)}, x_2 = {round(rb, 3)}, f'({round(lb, 3)}) = {round(first_derivative(lb), 3)}, f'({round(rb, 3)}) = {round(first_derivative(rb), 3)}, "
            f"x_md = {round(x_middle, 3)}, "
            f"f'(x_md) = {gradient_x_middle}.")

        if gradient_x_middle > 0:
            rb = x_middle
        elif gradient_x_middle < 0:
            lb = x_middle

        print("_"*50)


def secant_method(lb, rb):
    for i in range(3):

        print(f"Ітерація: {i + 1}")

        x_line = rb - ((first_derivative(rb) * (rb - lb)) / (
                   first_derivative(rb) - (first_derivative(lb))))
        gradient_x_line = first_derivative(x_line)
        print(
            f"x_1 = {round(lb, 3)}, x_2 = {round(rb, 3)}, f'({round(lb, 3)}) = {round(first_derivative(lb), 3)}, f'({round(rb, 3)}) = {round(first_derivative(rb), 3)}, "
            f"x* = {round(x_line, 3)}, "
            f"f'(x*) = {round(gradient_x_line, 3)}.")

        if gradient_x_line > 0:
            rb = x_line
        elif gradient_x_line < 0:
            lb = x_line

        print("_" * 50)

# newton_raphson(0.1)
# middle_point(0.1, 2)
secant_method(0.1, 2)