#!/usr/bin/python3
"""Python Script to generate HTML trough markdon syntax"""
import sys
import os
import markdown

if __name__ == "__main__":

    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        exit(1)

    elif os.path.exists(sys.argv[1]) is False:
        print("Missing " + sys.argv[1], file=sys.stderr)
        exit(1)

    else:
        src_file = open(sys.argv[1], "r")
        dest_file = open(sys.argv[2], "w")

        # html conversion
        hmtl = markdown.markdown(src_file.read())
        # send the content to the new file
        dest_file.write(hmtl + '\n')
        src_file.close()
        dest_file.close()
        exit(0)
