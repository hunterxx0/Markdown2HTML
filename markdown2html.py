#!/usr/bin/python3
""" Verify arguments """
import sys
from os import path
from string import ascii_letters

if __name__ == "__main__":
	def count_d(marker):
		c = 0
		for i in marker:
			if i == '#':
				c += 1
			if i == ' ':
				break
		return c


	if len(sys.argv) != 3:
		print('Usage: ./markdown2html.py README.md README.html' ,file=sys.stderr)
		exit(1)
	if not path.exists(sys.argv[1]):
		print('Missing {}'.format(sys.argv[1]) ,file=sys.stderr)
		exit(1)
	with open(sys.argv[1], 'r') as f:
		lines = []
		flag = 0
		for line in f.readlines():
			# </ol> handling
			if flag == 2 and line[:1] != '*':
				lines.append('</ol>\n')
				flag = 0
			# </ul> handling
			if flag == 1 and line[:1] != '-':
				lines.append('</ul>\n')
				flag = 0
			# <h> handling
			if line[:1] == '#':
				c = count_d(line)
				lines.append('<h{0}>{1}</h{0}>\n'.format(c, line[c+1:-1]))
			# <ul> handling
			if line[:1] == '-':
				if flag == 0:
					lines.append('<ul>\n')
					flag = 1
				lines.append('<li>{}</li>\n'.format(line[2:-1]))
			# <ol> Handling
			if line[:1] == '*':
				if flag == 0:
					lines.append('<ol>\n')
					flag = 2
				lines.append('<li>{}</li>\n'.format(line[2:-1]))
			# <p> handling
			if line[:1] in list(ascii_letters):
				if flag == 3:
					lines.append('<br />\n')
				if flag == 0:
					lines.append('<p>\n')
					flag = 3
				lines.append(line[:])
			if line[:1] == '\n' and flag == 3:
				lines.append('</p>\n')
				flag = 0
		if flag != 0:
			if flag == 1:
				lines.append('</ul>\n')
			if flag == 2:
				lines.append('</ol>\n')	
			if flag == 3:
				lines.append('</p>\n')	
		with open(sys.argv[2], 'a') as wr:
			for i in lines:
				wr.write(i)