# -*- coding: utf-8 -*-

import re

# children, by human DNA age analysis.
# cats. It doesn't differentiate individual breeds.
# samoyeds, 
# pomeranians, 
# akitas, and 
# vizslas.
# goldfish. No other kinds of fish.
# trees, all in one group.
# cars, presumably by exhaust or gasoline or something.
# perfumes



def readSues(filename):
    sues = []
    re_sue = re.compile('\w+: \d+')
    re_digits_only = re.compile('(\d+)')
    with open(filename) as datafile:    
        for thisstring in datafile:
            thissue =  {}
            m = re_sue.findall(thisstring)
            for amatch in m:
                aname,aval = amatch.split(':')
                #aval = re_digits_only.findall(aval)[0]
                thissue[aname] = int(aval)                
            sues.append(thissue)
    return sues
    
def calculateMatchValue(incompleteObject, knownObject):
    """Calculate an integer match value, scoring +1 for each match"""
    matchvalue = 0
    for catkey, catval in incompleteObject.items():
        if knownObject[catkey] == catval:
            matchvalue += 1
    return matchvalue

def calculateMatchValueWithRanges(incompleteObject, knownObject):
    """Calculate an integer match value, scoring +1 for each match"""
    matchvalue = 0
    for catkey, catval in incompleteObject.items():
        if (catkey == 'cats' or catkey=='trees'):
            if catval > knownObject[catkey]:
                matchvalue += 1
        elif (catkey == 'pomeranians' or catkey=='goldfish'):
            if catval < knownObject[catkey]:
                matchvalue += 1
        else:
            if knownObject[catkey] == catval:
                matchvalue += 1
    return matchvalue        

if __name__ == "__main__":
    """Day16:  Sue matching"""

    sues = readSues('day16.dat')
    
    mysue = { 'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, \
              'akitas': 0, 'vizslas': 0, 'goldfish': 5, 'trees': 3, \
              'cars': 2, 'perfumes': 1 }

    isue = 0
    maxsue = 0
    maxval = 0
    for checksue in sues:
        isue = isue + 1
        matchval = calculateMatchValue(checksue, mysue)
        print('Sue {0} match value {1}'.format(isue,matchval))
        if (matchval > maxval):
            maxval = matchval
            maxsue = isue
    
    print('Closest match is Sue {0}, with val {1}'.format(maxsue,maxval))
    # solution for part 1:  40
    
    isue = 0
    maxsue = 0
    maxval = 0
    for checksue in sues:
        isue = isue + 1
        matchval = calculateMatchValueWithRanges(checksue, mysue)
        print('Sue {0} match value {1}'.format(isue,matchval))
        if (matchval > maxval):
            maxval = matchval
            maxsue = isue
    
    print('Closest match is Sue {0}, with val {1}'.format(maxsue,maxval))
    # solution for part 1:  40
    
    
