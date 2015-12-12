# -*- coding: utf-8 -*-

import re
import sys
import pprint

instructions = {}
values = {}

def isint(value):
    try:
        int(value)
        return True
    except:
        return False

class WireDef:
    def __init__(self, instructionstring):
        self.instructionstring = instructionstring.rstrip()
        # now parse it
        #print('Parsing instruction: {0}'.format(thisstring))
        #gj RSHIFT 1 -> hc
        #   wire/val OP wire/val -> wire
        #   wire/val -> wire
        #   NOT wire -> wire        
        toks = self.instructionstring.split(' ')
        self.name = toks[ len(toks)-1 ] # last is always this wire name
        if len(toks) == 5:
            self.arg1 = toks[0]
            self.arg2 = toks[2]
            self.op = toks[1]
            pass
        elif len(toks) == 3:
            self.op = 'EQUAL'
            self.arg1 = toks[0]
            pass
        elif len(toks) == 4:
            if toks[0] != 'NOT':
                print("Not NOT?: {0}".format(instructionstring))
                sys.exit()
            self.op = 'NOT'
            self.arg1 = toks[1]
            pass
        else:
            print("UNPARSABLE:  {}".format(instructionstring))
            sys.exit()

def parseIntOrResolve(thisText):
    if isint(thisText):
        return int(thisText)
    else:
        return resolve(thisText)

def resolve(whichwire):
    if whichwire in values:
        return values[whichwire]

    print("Resolving {0}".format(whichwire))
    
    thisIns = instructions[whichwire]
    
    retval = 0    
    if (thisIns.op == 'EQUAL'):
        retval = parseIntOrResolve(thisIns.arg1)
            
    elif (thisIns.op == 'NOT'):
        retval = parseIntOrResolve(thisIns.arg1)
        retval = ~retval
        
    elif (thisIns.op == 'AND'):
        val1 = parseIntOrResolve(thisIns.arg1)
        val2 = parseIntOrResolve(thisIns.arg2)
        retval = val1 & val2
        
    elif (thisIns.op == 'LSHIFT'):
        val1 = parseIntOrResolve(thisIns.arg1)
        val2 = parseIntOrResolve(thisIns.arg2)
        retval = val1 << val2        
        
    elif (thisIns.op == 'RSHIFT'):
        val1 = parseIntOrResolve(thisIns.arg1)
        val2 = parseIntOrResolve(thisIns.arg2)        
        retval = val1 >> val2        
        
    elif (thisIns.op == 'OR'):
        val1 = parseIntOrResolve(thisIns.arg1)
        val2 = parseIntOrResolve(thisIns.arg2)
        retval = val1 | val2
        
    else:
        print('unknown op in {0}:  {1}'.format(whichwire, thisIns.instructionstring))
        sys.exit()
    
    values[whichwire] = retval
    return retval
    
    
        
        

                

with open('day7.dat') as datafile:
    
    for thisstring in datafile:
        thisIns = WireDef(thisstring)
        instructions[thisIns.name] = thisIns
    
day1_a = resolve('a')

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(values)

print("Overriding wire B with {0}".format(day1_a))

instructions['b'] = WireDef("{0} -> b".format(day1_a))
values = {}

day2_a = resolve('a')
#pp.pprint(values)

print("Day2 a={0}".format(day2_a))

        
