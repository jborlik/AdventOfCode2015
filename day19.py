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
#        print("can I replace: \"{0}\"?".format(toks[i]))
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
    
    print('-----------Part Two-----------')

    THISDOESNOTWORK = 0
    if THISDOESNOTWORK:
        # BRUTE FORCE FAILS
        potentials = ['HF','NAl','OMg'] # easier than looking for e
        for iStep in range(1,20):
            print("Step {0} with {1} potentials".format(iStep, len(potentials)))
            nextpot = []
            for thispot in potentials:
                if len(thispot) < len(targetmolecule):  # molecules don't get smaller
                    somemore = doTransformations(thispot, transform_list)
                    try:
                        iWantThisOne = somemore.index(targetmolecule)
                        print("Got it!  In {0} steps".format(iStep))
                        break
                    except:
                        pass
                    nextpot.extend(somemore)
            
            potentials = nextpot


    # iterate through starterText tokens.
    re_tok = re.compile("[A-Z][a-z]*")
    
    toks = re_tok.findall(targetmolecule)
    numtoks = len(toks)
    numRn = 0
    numAr = 0
    numY = 0    
    for i in range(0,len(toks)):
        if toks[i]=="Rn":
            numRn += 1
        if toks[i] == "Ar":
            numAr += 1
        if toks[i] == "Y":
            numY += 1
    
    print("NumToks={0}, NumRn={1}, NumAr={2}, NumY={3}".format(numtoks,numRn,numAr,numY))
    print("Steps? {0}".format(numtoks-numRn-numAr-2*numY-1))
    