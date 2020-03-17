import argparse
import os
import random
from colorRange import colorRange_Instance

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


# Inspired by https://stackoverflow.com/questions/28999287/generate-random-colors-rgb

def random_color():
    # TODO: Should we avoid choosing dark colors which obscure the text?
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return "%02x%02x%02x" % (red, green, blue)


def get_story_list(lines):
    feature = lines[0].rstrip()
    projectColor = colorRange_Instance(100, "#FFFF00")  # This was changed from randomColor() to
    # colorRange_Instance

    # Make sure color is not a repeat from a different project
    while projectColor in colorFeatureMap:
        projectColor = colorRange_Instance(100, "#FFFF00")  # This was changed from randomColor() to
        # colorRangeInstance() to
        # reflect feature update

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
