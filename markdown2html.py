#!/usr/bin/python3
'''Python Script'''
import sys
import os

if __name__ == "__main__":
    file = sys.argv[1]

    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        exit(1)

    elif os.path.exists(file) is False:
        print("Missing " + file, file=sys.stderr)
        exit(1)

    else:
        exit(0)
