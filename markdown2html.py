#!/usr/bin/python3
'''
Converts Markdown files to HTML format.

Usage: ./markdown2html.py README.md README.html
'''

import sys
import os
import markdown

def main():
    '''Main function to run the script.'''
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        exit(1)
    elif os.path.exists(sys.argv[1]) is False:
        print("Missing " + sys.argv[1], file=sys.stderr)
        exit(1)
    else:
        # Open input and output files
        src_file = open(sys.argv[1], "r")
        dest_file = open(sys.argv[2], "w")

        # Convert Markdown to HTML
        hmtl = markdown.markdown(src_file.read())

        # Write HTML content to output file
        dest_file.write(hmtl + '\n')

        # Close files and exit
        src_file.close()
        dest_file.close()
        exit(0)

if __name__ == '__main__':
    main()
