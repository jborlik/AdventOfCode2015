# -*- coding: utf-8 -*-

import json

summedcount = 0

def parsedInt(thisint):
    global summedcount
    summedcount += int(thisint)
    return thisint

def countIfInt(sPotentialInt):
    try:
        return int(sPotentialInt)
    except:
        return 0

def countListItems(aList):
    thiscount = 0
    for aEntry in aList:
        if isinstance(aEntry, list):
            thiscount += countListItems(aEntry)
        elif isinstance(aEntry, dict):
            thiscount += dontCountRedObjects(aEntry)
        else:
            thiscount += countIfInt(aEntry)
    return thiscount

def dontCountRedObjects(parsedDict):
    thiscount = 0
    for attr,value in parsedDict.items():
        if value == 'red':
            thiscount = 0
            break
        else:
            if isinstance(value, list):
                # handle each object type in the list, too
                thiscount += countListItems(value)
                    
            elif isinstance(value, dict):
                thiscount += dontCountRedObjects(value)
                
            else:
                thiscount += countIfInt(value)

    return thiscount    
    

if __name__ == "__main__":
    """Day 12, json parsing"""
    
    with open('day12.dat') as datafile:
        
        parsedobj = json.load(datafile, parse_int=parsedInt)
        
    
    print('Count={0}'.format(summedcount))
    # answer = 119433
    
    unredcount = dontCountRedObjects(parsedobj)
    
    print('Non-red count={0}'.format(unredcount))