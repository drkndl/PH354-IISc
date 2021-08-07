"""
Author: Drishika Nadella
Date: 20th April 2021, Tuesday
Time: 12:40 PM
Email: drishikanadella@gmail.com 
"""

import numpy as np

def cartopolar(x,y):
    """
    This function converts cartesian coordinates into polar coordinates.
    x is the x-coordinate in the cartesian system.
    y is the y-coordinate in the cartesian system.
    The function returns r (distance from the pole) and theta (angle from the directed line) in degrees.
    """
    r = np.sqrt(x**2 + y**2)
    if x>0:
        theta = np.arctan(y/x)  # in radians
    else:
        theta = np.arctan(y/x) + np.pi   # in radians

    return r, round(np.degrees(theta), 2)  # angle in degrees, rounded off to 2 decimals

print(cartopolar(3,4))

print(cartopolar(-12,-5))
