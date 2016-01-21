#!/usr/bin/python

import os, sys
from os.path import basename
from subprocess import call
dirs = os.listdir( "." )

call(["lessc", "./styles/main.less", "./main.css"])
# This would print all the files and directories
for file in dirs:
    if file.endswith(".md"):
        baseName = os.path.splitext(file)[0]
        cmdArgs = ["markdown-html", file, "-o", "html/" +baseName + ".html", "-l", "template.html", "-s", "main.css"]
        #if len(sys.argv) > 1:
        #    cmdArgs.extend(["-s", sys.argv[1]])
        # print cmdArgs
        call(cmdArgs)
