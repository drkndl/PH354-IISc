"""
Author: Drishika Nadella
Date: 20th April 2021
Time: 1430
Contact: drishikanadella@gmail.com 
"""

import numpy as np

def relativity(x, v):
    """
    This function calculates the time elapsed for an Earth bound observer and comparing it with that of an astronaut
    travelling in a relative rocket. It displays the concept of special relativity. Here,
    x = distance travelled by the rocket in light years
    v = velocity of the relativistic rocket as a ratio to c.
    It calculates the time elapsed for passenger in the rocket, T and the time in rest frame, t and prints these values.
    """
    T = x/v
    gamma = 1/np.sqrt(1-v**2)
    t = T/gamma

    print("Time in the rest frame of the observer: %f years"% (T))
    print("Time for passenger aboard the spaceship: %f years"% (t))

relativity(10, 0.99)
