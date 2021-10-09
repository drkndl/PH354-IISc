"""
Author: Drishika Nadella
Date: 18th May 2021
Time: 1534
Contact: drishikanadella@gmail.com
"""

import numpy as np
import matplotlib.pyplot as plt

A = 1
B = G = 0.5
D = 2

def x_func(a, b):
    return A*a - B*a*b

def y_func(a, b):
    return G*a*b - D*b

def rk4(h, x, y, n):
    if n==1:
        k1 = h*x_func(x, y)
        k2 = h*x_func(x + h/2, y + k1/2)
        k3 = h*x_func(x + h/2, y + k2/2)
        k4 = h*x_func(x + h, y + k3)
    else:
        k1 = h*y_func(x, y)
        k2 = h*y_func(x + h/2, y + k1/2)
        k3 = h*y_func(x + h/2, y + k2/2)
        k4 = h*y_func(x + h, y + k3)
    return k1/6 + k2/3 + k3/3 + k4/6

h = 0.001
tarr = np.arange(0, 30, h)
xarr = [2]
yarr = [2]

for t in tarr:
    xarr.append(xarr[-1] + rk4(h, xarr[-1], yarr[-1], 1))
    yarr.append(yarr[-1] + rk4(h, xarr[-1], yarr[-1], 2))

plt.plot(tarr, xarr[:-1], label="Population of rabbits")
plt.plot(tarr, yarr[:-1], label="Population of foxes")
plt.xlabel("Time")
plt.ylabel("Population")
plt.title("Lotka-Volterra Model")
plt.legend()
plt.show()
