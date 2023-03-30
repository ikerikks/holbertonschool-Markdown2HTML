#!/usr/bin/python3
import sys
import os

""" Python script """

file = "README.md"

if len(sys.argv) < 2:
    print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
    exit(1)

elif os.path.exists(file) is False:
    print("Missing " + file, file=sys.stderr)
    exit(1)

else:
    exit(0)
