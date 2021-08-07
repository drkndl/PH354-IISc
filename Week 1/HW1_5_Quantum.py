"""
Author: Drishika Nadella
Date: 20th April 2021
Time: 1432
Email: drishikanadella@gmail.com
"""

import numpy as np

# Defining the global variables
h = 4.135*10**(-15)  # Planck's constant in eV/Hz
hb = h/(2*np.pi)    # Reduced Planck's constant

def potential(m, E, V):
    """
    This function calculates the probability of particle transmission and reflection in a 1-D potential step.
    Here, m is the mass of the particle.
    E is the kinetic energy of the particle.
    V is the height of potential energy jump.
    The two wavevectors k1 and k2 calculated below correspond to the wavenumber at initial kinetic energy,
    and the wavenumber after the potential jump.
    R is the reflection probability and T is the transmission probability.
    The function returns R and T.
    """

    k1 = np.sqrt(2*m*E)/hb
    k2 = np.sqrt(2*m*(E-V))/hb

    # Reflection probability
    R = ((k1-k2)/(k1+k2))**2

    # Transmission probability
    T = 1 - R

    return R, T

m = 9.11*10**(-31)
E = 10
V = 9

R, T = potential(m, E, V)
print("Probability of particle reflection: %.2f"% (R))
print("Probability of particle transmission: %.2f"% (T))
