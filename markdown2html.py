#!/usr/bin/python3
'''Python Script'''
import sys
import os

if __name__ == "__main__":

    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        exit(1)

    elif os.path.exists(sys.argv[1]) is False:
        print("Missing " + sys.argv[1], file=sys.stderr)
        exit(1)

    else:
        exit(0)
