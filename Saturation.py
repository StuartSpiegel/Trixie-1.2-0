import colorsys
import random


# Only get Colors in the light end of the color spectrum
def getLightColor():
    h, s, l = random.random(), 0.5 + random.random() / 2.0, 0.4 + random.random() / 5.0
    r, g, b = [int(256 * i) for i in colorsys.hls_to_rgb(h, l, s)]
    return "%02x%02x%02x" % (r, g, b)
