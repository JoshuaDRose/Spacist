"""
utils.py
Handles miscellaneous functions.
"""

import random

def generate_color() -> list:
    """ Generates random RGB value, mainly for enemy class """
    rgb = [0,0,0]
    for i in range(len(rgb)):
        rgb[i] = random.randint(0,255)
    return rgb
