# -*- coding: utf-8 -*-

import re
import sys

# The only escape sequences used are:
#   \\ (which represents a single backslash), 
#   \" (which represents a lone double-quote character), 
#   and \x plus two hexadecimal characters (which represents a single character with that ASCII code)
re_test1 = re.compile(r'\\\\')
re_test2 = re.compile(r'\\"')
re_test3 = re.compile(r'\\x[0-9a-f]{2,2}')


totalcodechars = 0
totalmemchars = 0

with open('day8.dat') as datafile:
    
    for thisstring in datafile:
        thisstring = thisstring.rstrip()
        codechars = len(thisstring)
        totalcodechars += codechars
        
        # remove start/end quotes
        thisstring = thisstring[1:-1]
        # resolve \\  to 0
        thisstring = re_test1.sub('0', thisstring)
        # resolve \"  to 0
        thisstring = re_test2.sub('0', thisstring)
        # resolve \xHH to 0
        thisstring = re_test3.sub('0', thisstring)
        
        memchars = len(thisstring)
        totalmemchars += memchars

print("Code chars = {0}, mem chars = {1}, diff = {2}".format(totalcodechars,totalmemchars,totalcodechars-totalmemchars))
    

print("Part Two")
re_slash = re.compile(r'\\')
totalcodechars = 0
totalencodedchars = 0
        
with open('day8.dat') as datafile:
    
    for thisstring in datafile:
        thisstring = thisstring.rstrip()
        totalcodechars += len(thisstring)
        
        thisstring = thisstring[1:-1] # remove starting/ending quotes, as they can screw up things like "hey\\"
        thisstring = re_slash.sub(r'\\\\', thisstring)
        thisstring = re_test2.sub(r'\\\\"', thisstring)
        totalencodedchars += len(thisstring)+4+2
    
print("Code chars = {0}, encoded chars = {1}, diff = {2}".format(totalcodechars,totalencodedchars,totalencodedchars-totalcodechars))
# 1815 low, 2090 high, 2085 just right