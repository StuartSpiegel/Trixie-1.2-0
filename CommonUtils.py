import argparse
import os
import random

# CommonUtils.py acts as a helper function for PopulateStickies.py

# Keep track of used colors
colorFeatureMap = {}


# Read in stories from text file
# TODO: Eventually pull straight from wiki
def read_input():
    parser = argparse.ArgumentParser()
    parser.add_argument("wiki_files_directory",
                        help="C:\\Users\\stuar\\Desktop\\Trixie\\Trixie-1.2-0-master\\Docs1")
    wiki_files_directory = parser.parse_args().wiki_files_directory

    storyList = []
    # Have to pass the encoding format here when opening the file, this avoids a decode byte error. (,encoding="utf-8")
    for filename in os.listdir(wiki_files_directory):
        file = open(wiki_files_directory + "/" + filename)
        lines = file.readlines()
        storyList += get_story_list(lines)
        file.close()
    return storyList, colorFeatureMap


def lighten_color(color, amount=0.5):
    """
    Lightens the given color by multiplying (1-luminosity) by the given amount.
    Input can be matplotlib color string, hex string, or RGB tuple.

    Examples:
    >> lighten_color('g', 0.3)
    >> lighten_color('#F034A3', 0.6)
    >> lighten_color((.3,.55,.1), 0.5)
    """
    import matplotlib.colors as mc
    import colorsys
    try:
        c = mc.cnames[color]
    except:
        c = color
    c = colorsys.rgb_to_hls(*mc.to_rgb(c))
    return colorsys.hls_to_rgb(c[0], max(0, min(1, amount * c[1])), c[2])


# Inspired by https://stackoverflow.com/questions/28999287/generate-random-colors-rgb
def random_color():
    # TODO: Should we avoid choosing dark colors which obscure the text?
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return "%02x%02x%02x" % (red, green, blue)


# A Percentage of 0.0% will return the same color and 1.0 will return white
# Everything in between will be a lighter shade of the same HUE. Imagine moving along a line between your selected
# color and the pure white on an HSB model.
# color is the base color selector to choose between white.
def lighter(percent):
    color = random_color()
    white = (255, 255, 255)
    vector = white - color
    return color + vector * percent


def get_story_list(lines):
    feature = lines[0].rstrip()
    projectColor = lighten_color(random_color(), amount=0.5)  # This was changed from randomColor() to
    # lighter_color

    # Make sure color is not a repeat from a different project
    while projectColor in colorFeatureMap:
        projectColor = lighten_color(random_color(), amount=0.5)  # This was changed from randomColor() to
        # lighter_color

    colorFeatureMap[projectColor] = feature

    # Parse stories from text file
    startIndex = 0
    for i in range(len(lines)):
        if "==Stories" in lines[i]:
            startIndex = i + 1
            break

    storyList = []
    storyCategory = ""
    for line in lines[startIndex: len(lines)]:
        if line.startswith("==="):
            stripAfter = line.find("(")
            storyCategory = line[3:stripAfter]
        elif line.startswith("* "):
            stripAfter = line.rfind("(")
            storyDescription = line[2:stripAfter]
            storySize = line[stripAfter + 1: line.rfind(")")]
            storyInfo = (storyCategory, storyDescription, [], storySize, feature, projectColor)
            storyList.append(storyInfo)
        elif line.startswith("**") and storyInfo:
            storyInfo[2].append(line[3:].rstrip())
        elif line.startswith("-") and storyInfo:  # The "-" sentinel value will serve as the parse indicator for
            # Acceptance Criteria
            storyInfo[3].append(line[4].rstrip())
    return storyList
