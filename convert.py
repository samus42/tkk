#!/usr/bin/python

import os, sys
from os.path import basename
from subprocess import call
dirs = os.listdir( "." )

# This would print all the files and directories
for file in dirs:
    if file.endswith(".md"):
        print file
        baseName = os.path.splitext(file)[0]
        call(["markdown-html", file, "-o", "html/" +baseName + ".html"])
