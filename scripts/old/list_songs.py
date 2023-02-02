#!/usr/bin/env python3

import glob
import subprocess

def getSongDirs():
    return glob.glob("./*")

def read_lines_from_file(filename):
    lines = []
    with open('./' + filename, 'r') as f:
        lines = f.readlines()
    return lines


if __name__ == "__main__":
    songsDir = getSongDirs()
    songsDir.sort()
    for songDir in songsDir:
        lines = read_lines_from_file(songDir + "/" + "README.md")
        songNumber = lines[0].split("_")[-1].strip()
        songText = lines[1].strip()
        print(songNumber + ", " + songText)