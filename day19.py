# -*- coding: utf-8 -*-

# Day 19: More transformations and counting permutations

import re

def readTransformationFile(myfilename):
    transformations = []
    startertext = ''
    with open(myfilename) as datafile:
        for thisstring in datafile:    
            thisstring = thisstring.rstrip()
            toks = thisstring.split(' ')
            if len(toks) == 3:
                transformations.append( (toks[0], toks[2]) )
            elif len(toks) == 1:
                startertext = thisstring
                
            
    return startertext, transformations

def doTransformations(starterText, transformList):
    transformed = []
    
    # iterate through starterText tokens.
    re_tok = re.compile("[A-Z][a-z]*")
    
    toks = re_tok.findall(starterText)
    for i in range(0,len(toks)):
        print("can I replace: \"{0}\"?".format(toks[i]))
        for tfrom,tto in transformList:
            if toks[i]==tfrom:
                # replace
                newlist = list(toks)
                newlist[i] = tto
                transformed.append( ''.join(newlist))
            
    transformed = list(set(transformed)) # get unique values
    return transformed
    

if __name__ == "__main__":
    """Day19:  Transformations on text"""

    print("----------Testing-----------")
    test_transform_list = [ ('H', 'HO'), ('H','OH'), ('O','HH') ]
    test_starter = "HOH"
    
    transformed = doTransformations(test_starter,test_transform_list)
    print(transformed)
    
    print('---------Part One----------')
    targetmolecule, transform_list = readTransformationFile('day19.dat')
    
    #print("Starter text={0}".format(starttext))
    #print(transform_list)
    
    transformed = doTransformations(targetmolecule, transform_list)
    
    print("Number of transforms = {0}".format(len(transformed)))