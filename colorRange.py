from random import random


# Generates a random String representing a color in HEX


# def generateRandomColorHex():
# number_of_colors = 8
# color = ["#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
# for i in range(number_of_colors)]
# print(color)
# return color
# This block shows a chart for testing the color instances.
# for i in range(number_of_colors):
#   plt.scatter(random.randint(0, 10), random.randint(0, 10), c=color[i], s=200)
# plt.show()


# A Percentage of 0.0% will return the same color and 1.0 will return white
# Everything in between will be a lighter shade of the same HUE. Imagine moving along a line between your selected
# color and the pure white on an HSB model.
# color is the base color selector to choose between white.
# def lighter(percent):
# color = random_color()
# white = [255, 255, 255]
# vector = white - color
# return color + vector * percent


# Creates an array of colors by calling the lighter method --> NumSamples amount of times (iterations)
# def colorRange_Instance(numSamples, baseColor):
#  theColors = [numSamples]
# for i in theColors:
#  theColors[i] = lighter(0.85)


def getRGB_Instance():
    rgbl = [255, 0, 0]
    random.shuffle(rgbl)
    return tuple(rgbl)
