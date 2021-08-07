"""
Author: Drishika Nadella
Date: 20th April 2021
Time: 16:09PM
Email: drishikanadella@gmail.com
"""

import numpy as np
import matplotlib.pyplot as plt

# Creating a list with the zeroth Catalan number
C = [1]
# Creating the counter
i = 0

# Calculating and printing Catalan numbers upto 1 billion
while C[-1] <= 10**9:
    print(C[-1])
    C.append((4*i + 2)/(i+2)*C[i])
    i+=1

# Plotting the Catalan numbers
plt.plot(range(len(C)), C, marker='o')
plt.title("Visualizing the Catalan numbers upto 1 billion")
plt.show()
