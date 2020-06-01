import argparse
import os
import random

# CommonUtils.py acts as a helper function for PopulateStickies.py
from Saturation import getLightColor

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
    # Might Have to pass the encoding format here when opening the file, this avoids a decode byte error. (,
    # encoding="utf-8")
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
    feature = lines[0].rstrip()  # Remove trailing characters at the end of the line
    projectColor = getLightColor()  # This was changed from randomColor() to
    # getLightColor()

    # Make sure color is not a repeat from a different project
    while projectColor in colorFeatureMap:
        projectColor = getLightColor()  # This was changed from randomColor() to
        # getLightColor()

    colorFeatureMap[projectColor] = feature

    # local variables
    storyList = []
    storyCategory = ""
    acceptanceCriteria = ""
    testing = ""
    considerations = ""

    # Set the initial range of lines to search for fields within, parse from the first sentinel string to file
    # length. redefine the start index on each new parse.

    # startIndex = 0
    # for k in range(len(lines)):
    #  if "==Acceptance" or "==Considerations" or "==Stories" in lines[k]: # searching for headings, use for loop to
    # iterate over range of lines for field categories. We know each category starts at a certain range,
    # use blank line as sentinel value to know when to stop
    #    startIndex = k + 1
    #    break

    startIndex = 0
    nextBlank = 0
    toParse = []
    for k in range(len(lines)):
        if isEmptyLine(lines[k]):  # Search for the first blank line
            nextBlank = k

        if "==Acceptance" in lines[k]:
            startIndex = k + 1  # set the start index (line) to be next line after acceptance criteria
            for j in range(startIndex, nextBlank):  # We want to parse everything from the acceptance Criteria line
                # down to the next blank
                acceptanceCriteria += j
        elif "==Considerations" in lines[k]:
            startIndex = k + 1  # adjust the start index
            for m in range(startIndex, nextBlank):
                considerations += m
        elif "==Stories" in lines[k]:
            startIndex = k + 1  # adjust the start index
            for v in range(startIndex, nextBlank):
                storyList += v

    # In the range of line[0 to lines.length]
    for line in lines[startIndex: len(lines)]:
        if line.startswith("==="):  # look for the sentinel value of "===" meaning the line to strip is either
            # categories: testing, research, or Design and Development
            stripAfter = line.find("(")
            # Get the storyCategory
            storyCategory = line[3:stripAfter]  # Get the story category after the initial offset
            # Get the testing field
            stripAfter = line.find("Testing")  # redefine the offset for the next parse
            testing = line[2:stripAfter]  # Get the testing field
        # clause looking for values that only have the sentinel value of "=="
        elif line.startswith("=="):
            stripAfter = line.find("Acceptance Criteria")
            # Get the acceptance criteria
            acceptanceCriteria = line[2:stripAfter]

            # separate the two cases
            # Get the considerations field
            stripAfter = line.find("Considerations")
            considerations = line[2:stripAfter]

        # clause looking for asterisk indicating story descriptors (bullets *)
        elif line.startswith("* "):
            stripAfter = line.rfind("(")
            storyDescription = line[2:stripAfter]
            # Get the storySize by calculating from last parse point to closing brace
            storySize = line[stripAfter + 1: line.rfind(")")]

            # pack collected data into the storyInfo array to be appended to storyList for use by functions
            storyInfo = (
                storyCategory, storyDescription, [], storySize, feature, projectColor, acceptanceCriteria,
                testing, considerations)
            # Add the parsed storyInfo to the storyList to populate the DocX
            storyList.append(storyInfo)
            # clause is looking for double asterisk indicating that story Info is following, append to storyInfo
        elif line.startswith("**") and storyInfo:
            storyInfo[2].append(line[3:].rstrip())
    return storyList


def isEmptyLine(string):
    global x
    if len(string == 0):
        x = True
    elif len(string > 0):
        x = False
    return bool(x)
