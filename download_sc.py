#!/usr/local/bin/python3

import os

f = open("data/sc_data.txt")

os.chdir("music/sc")

for line in f:
    parts = line.split("|")
    url = parts[3]

    paths = url.split("/")

    os.system("soundscrape %s -t %s" % (paths[3], paths[4]))




