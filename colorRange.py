import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap


def colorFader(c1, c2, mix=0):  # fade (linear interpolate) from color c1 (at mix=0) to c2 (mix=1)
    c1 = np.array(mpl.colors.to_rgb(c1))
    c2 = np.array(mpl.colors.to_rgb(c2))
    return mpl.colors.to_hex((1 - mix) * c1 + mix * c2)


# (N) the number of gradient colors to generate in between the Color range (Color c1) and (Color c2).
c1 = '#1f77b4'  # blue -First Color in the Gradient Range
c2 = 'green'  # green -Second Color in the Gradient Range
n = 500

fig, ax = plt.subplots(figsize=(8, 5))
for x in range(n + 1):
    ax.axvline(x, color=colorFader(c1, c2, x / n), linewidth=4)
plt.show()


# Generates a color map from a single parameter
def bluegreen(y):
    red = [(0.0, 0.0, 0.0), (0.5, y, y), (1.0, 0.0, 0.0)]
    green = [(0.0, 0.0, 0.0), (0.5, y, y), (1.0, y, y)]
    blue = [(0.0, y, y), (0.5, y, y), (1.0, 0.0, 0.0)]
    colordict = dict(red=red, green=green, blue=blue)
    bluegreenmap = LinearSegmentedColormap('bluegreen', colordict, 256)
    return bluegreenmap

