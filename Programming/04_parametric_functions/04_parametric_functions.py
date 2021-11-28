
import sympy as sp
import numpy as np
import matplotlib.pyplot as plot


def draw_parametric_curve(t_values, func_x, func_y):
    t = sp.Symbol('t')
    lambda_x = sp.lambdify(t, func_x, "numpy")
    lambda_y = sp.lambdify(t, func_y, "numpy")

    x_values = [lambda_x(i) for i in t_values]
    y_values = [lambda_y(i) for i in t_values]
    plot.plot(x_values, y_values, color='#c4c4c4')


def draw_function(t_values, step, func_x, func_y, func_g):
    t = sp.Symbol('t')
    s = sp.Symbol('s')
    s_val = 0
    gx_vals = []
    gy_vals = []

    for t_val in t_values:
        s_val += step * sp.sqrt(sp.diff(func_x, t).subs(t, t_val)**2 + sp.diff(func_y, t).subs(t, t_val)**2)
        gx_vals.append(func_x.subs(t, t_val) +
                       (func_g.subs(s, s_val) /
                        sp.sqrt(sp.diff(func_x, t).subs(t, t_val)**2 + sp.diff(func_y, t).subs(t, t_val)**2)) *
                       sp.diff(func_y, t).subs(t, t_val))
        gy_vals.append(func_y.subs(t, t_val) +
                       (func_g.subs(s, s_val) /
                        sp.sqrt(sp.diff(func_x, t).subs(t, t_val)**2 + sp.diff(func_y, t).subs(t, t_val)**2)) *
                       (-sp.diff(func_x, t).subs(t, t_val)))

    plot.plot(gx_vals, gy_vals, color='#690415')

def __main__():
    print('Input parametric defined curve L:')
    func_x = sp.sympify(input('x(t) = '))
    func_y = sp.sympify(input('y(t) = '))
    print('Input periodic function g(s):')
    func_g = sp.sympify(input('g(s) = '))

    a, b = map(float, input('Input [a, b]: ').split())
    step = float(input('Input step: '))

    t_values = [i for i in np.arange(a, b, step)]
    draw_parametric_curve(t_values, func_x, func_y)
    draw_function(t_values, step, func_x, func_y, func_g)
    plot.gca().set_aspect('equal')
    plot.show()


if __name__ == '__main__':
    __main__()
