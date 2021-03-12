# -*- coding: utf-8 -*-
"""
Created on Sat May 13 01:29:33 2017

@author: DIP
"""

from nltk.parse.stanford import StanfordParser

sentence = 'The quick brown fox jumps over the lazy dog'



# get parse tree
result = list(scp.raw_parse(sentence)) 
tree = result[0]

# print the constituency parse tree
print(tree) 

# visualize constituency parse tree
tree.draw() 
