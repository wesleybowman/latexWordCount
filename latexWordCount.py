'''
    latexWordCount counts the words in a .tex file.
    Copyright (C) 2013 Wesley A. Bowman

    This program is free software; you can redistribute it and/or modify 
    it under the terms of the GNU General Public License as published by 
    the Free Software Foundation; either version 2 of the License, or 
    (at your option) any later version.

    This program is distributed in the hope that it will be useful, 
    but WITHOUT ANY WARRANTY; without even the implied warranty of 
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. 
    See the GNU General Public License for more details.

    You should have received a copy of the GNU General Public License 
    along with this program; if not, write to the 
    Free Software Foundation, Inc., 59 Temple Place, 
    Suite 330, Boston, MA 02111-1307 USA

'''

import os
import sys

#Sets a list of key words that latex uses for formating
keywords = ['\\begin', '\\end', '\\section',
             '\\subsection', '\\usepackage', 
             '\\hline', '\\caption', '\\lipsum', 
             '\\label', '\\\\', '\r\n', '\\item', 
             '\\textbf', '\\', '[', ']', '{', '}', '&',
             '$','$$','\\frac','\\cite','\\ref','\\$']


def text_breaker(list_of_strings):
    '''Function takes a list of strings and outputs a list of words.
        Traverses list, uses string.split() on each entry in the list '''
    new_list = []    
    for line in list_of_strings:
        for word in line.split():
            new_list.append(word)
    return new_list

def keyword_filter(word):
    '''Function check to see if word is in key list'''
    for keyword in keywords:
        if word.startswith(keyword) or word.endswith(keyword):
            return True    
    return False    

if __name__=='__main__':
	# Open specified file
	infileName = raw_input('Name of file: ')
	infileName +='.tex'
	infile = os.path.abspath(infileName)

	with open(infile, 'r') as infile:
		# Pass list of lines to text var
		text = infile.readlines()


	#list of words, includes punctuation and keywords
	text = text_breaker(text)

	#traverse list and count up the words
	count=0
	for item in text:
		if not keyword_filter(item):
			count+=1

	#print word count
	print '\n%s words \n'%(count,)
	x=raw_input('Press any key to exit')
	sys.exit()