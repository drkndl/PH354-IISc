"""
Author: Drishika Nadella
Date: 18th May 2021
Time: 1640
Contact: drishikanadella@gmail.com
"""

import numpy as np
import matplotlib.pyplot as plt

def func(V_in, V_out, RC):
    return (V_in - V_out)/RC

def rk4(h, x, y, RC):
    k1 = h*func(x, y, RC)
    k2 = h*func(x + h/2, y + k1/2, RC)
    k3 = h*func(x + h/2, y + k2/2, RC)
    k4 = h*func(x + h, y + k3, RC)
    return k1/6 + k2/3 + k3/3 + k4/6

h = 0.000001
tarr = np.arange(0, 11, h)
vout = [0]
vin = []
for t in tarr:
    if t==0:
        vin.append(vout[0])
    elif np.floor(2*t)%2 == 0:
        vin.append(1)
    else:
        vin.append(-1)

# Considering RC = 1

for t in tarr:
    i = 0
    vout.append(vout[-1] + rk4(h, vout[-1], vin[i], 0.01))
    i += 1

# plt.subplot(3, 1, 1)
plt.plot(tarr, vout[:-1])
plt.xlabel("Time")
plt.ylabel("Voltage")
plt.title("Low Pass Filter: RC = 1")
plt.show()
