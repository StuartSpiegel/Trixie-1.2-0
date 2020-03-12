
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
    theColors = []
    for i in numSamples:
        theColors[i] = lighter(baseColor, 0.5)


# Create a base selection of acceptable colors in a certain range of RGB values --> colorRange.py
# TODO: ADD random (numColors) colors (light colors only) to the array of acceptable colors
def select_Color_InRange():
    numColors = 25
    # Populate the colors list from a list of acceptable Colors, this list of acceptable colors was generated by
    # colorRange.py
    for i in numColors:
        colors = list(colorFader(c1, c2, mix=0))

    # The selector is the variable holding the index in the colors Array of the Color we will pick at Random. This color
    # list had been modified by colorRange.py
    selector = random.randint(0, len(colors))
    return colors.__getitem__(selector)
