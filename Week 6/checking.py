import numpy as np

Vout0 = 0
tee = np.linspace(0,10,100000)

def Vin(t):
    if (t==0): return Vout0
    if (int(np.floor(2*t)%2)==0): return 1
    return -1

print(tee)

for t in tee:
    print(Vin(t))
