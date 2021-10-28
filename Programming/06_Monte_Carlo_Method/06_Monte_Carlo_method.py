
import matplotlib.pyplot as plot
import sympy as sp
import numpy as np
import random


def generate_function_values(func, x_vals: list):
    func_y = sp.lambdify(x, func, "numpy")
    return [func_y(x_vals[i]) for i in range(len(x_values))]


def is_dot_in_area(x_val, y_val, func_f, func_g):
    fy = sp.lambdify(x, func_f, "numpy")
    gy = sp.lambdify(x, func_g, "numpy")
    if (y_val >= fy(x_val) and y_val <= gy(x_val)) or (y_val >= gy(x_val) and y_val <= fy(x_val)):
        return True
    return False


f = sp.sympify(input('Input f(x): \nf(x) = '))
g = sp.sympify(input('Input g(x): \ng(x) = '))
a, b = map(float, input('Input [a, b]: ').split())

x = sp.Symbol('x')

step = 0.01

x_values = [round(i, 3) for i in np.arange(a, b + step, step)]
fy_values = generate_function_values(f, x_values)
gy_values = generate_function_values(g, x_values)

dots_num = int(abs(b-a) * 1000)
random_dots_x = [random.uniform(a, b) for i in range(dots_num)]
random_dots_y = [random.uniform(min(min(fy_values), min(gy_values)),
                                max(max(fy_values), max(gy_values))) for i in range(dots_num)]
dots_in_area_x = []
dots_in_area_y = []
to_del = []

for i in range(len(random_dots_x)):
    if is_dot_in_area(random_dots_x[i], random_dots_y[i], f, g):
        to_del.append(i)
        dots_in_area_x.append(random_dots_x[i])
        dots_in_area_y.append(random_dots_y[i])

for i in range(len(to_del)):
    del random_dots_x[to_del[i] - i]
    del random_dots_y[to_del[i] - i]

square_of_main_rectangle = (abs(max(max(fy_values), max(gy_values)) - min(min(fy_values), min(gy_values)))) * \
                           (abs(b - a))
proportion = len(dots_in_area_x) / (len(random_dots_x) + len(dots_in_area_x))
square_of_shape = square_of_main_rectangle * proportion

print('Square: ' + str(round(square_of_shape, 5)))

plt = plot.plot(x_values,
                fy_values,
                color='#690415')
plot.scatter(random_dots_x,
             random_dots_y,
             color='#c7c7c7',
             s=0.5)
plot.vlines(a,
            ymin=min(min(fy_values), min(gy_values)),
            ymax=max(max(fy_values), max(gy_values)),
            color='#adadad',
            linestyles='dashed')
plot.vlines(b,
            ymin=min(min(fy_values), min(gy_values)),
            ymax=max(max(fy_values), max(gy_values)),
            color='#adadad',
            linestyles='dashed')
plot.hlines(max(max(fy_values), max(gy_values)),
            xmin=min(x_values),
            xmax=max(x_values),
            color='#adadad',
            linestyles='dashed')
plot.hlines(min(min(fy_values), min(gy_values)),
            xmin=min(x_values),
            xmax=max(x_values),
            color='#adadad',
            linestyles='dashed')
plot.scatter(dots_in_area_x,
             dots_in_area_y,
             color='#317d4a',
             s=0.5)
plot.plot(x_values,
          gy_values,
          color='#260469')
plot.show()
