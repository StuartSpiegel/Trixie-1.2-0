
import numpy as np
from matplotlib.colors import LinearSegmentedColormap


# Generates a color map from a single parameter
def bluegreen(y):
    red = [(0.0, 0.0, 0.0), (0.5, y, y), (1.0, 0.0, 0.0)]
    green = [(0.0, 0.0, 0.0), (0.5, y, y), (1.0, y, y)]
    blue = [(0.0, y, y), (0.5, y, y), (1.0, 0.0, 0.0)]
    colordict = dict(red=red, green=green, blue=blue)
    bluegreenmap = LinearSegmentedColormap('bluegreen', colordict, 256)
    return bluegreenmap


# A Percentage of 0.0% will return the same color and 1.0 will return white
# Everything in between will be a lighter shade of the same HUE. Imagine moving along a line between your selected
# color and the pure white on an HSB model.
# color is the base color selector to choose between white.
def lighter(color, percent):
    """assumes color is rgb between (0, 0, 0) and (255, 255, 255)"""
    color = np.array(color)
    white = np.array([255, 255, 255])
    vector = white - color
    return color + vector * percent


# Creates an array of colors by calling the lighter method --> NumSamples amount of times (iterations)
def colorRange_Instance(numSamples, baseColor):
    theColors = [numSamples]
    for i in theColors:
        theColors[i] = lighter(baseColor, 0.5)


