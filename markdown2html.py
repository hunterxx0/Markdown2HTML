#!/usr/bin/python3
""" Verify arguments """
import sys
from os import path

if __name__ == "__main__":
	if len(sys.argv) != 3:
		print('Usage: ./markdown2html.py README.md README.html' ,file=sys.stderr)
		exit(1)
	if not path.exists(sys.argv[1]):
		print('Missing {}'.format(sys.argv[1]) ,file=sys.stderr)
		exit(1)