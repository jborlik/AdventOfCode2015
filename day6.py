# -*- coding: utf-8 -*-

import re
import sys
import matplotlib.pyplot as plt
import numpy as np

re_test1 = re.compile(r'(\w+ ?\w*) (\d+),(\d+) through (\d+),(\d+)')

lights = np.zeros( (1000,1000), dtype=int )

instructions = []

iday = 2

with open('day6.dat') as datafile:
    
    for thisstring in datafile:
        
        #print('Parsing instruction: {0}'.format(thisstring))
        
        m = re_test1.match(thisstring)
        if m:
            if m.group(1) == 'turn off':
                dowhat = 0
            elif m.group(1) == 'turn on':
                dowhat = 1
            elif m.group(1) == 'toggle':
                dowhat = 2
            else:
                print('Unparsed action!')
                sys.exit()
            
            instructions.append( (dowhat, int(m.group(2)), int(m.group(3)), \
                                    int(m.group(4))+1, int(m.group(5))+1)  )
        else:
            print('Unparsed instruction!')
            sys.exit()

# now we have all of the instructions

for ins in instructions:
    thisview = lights[ ins[1]:ins[3], ins[2]:ins[4] ]
    
    if ins[0] == 0:
        # turn off
        print('turning off {0},{1} - {2},{3}'.format(ins[1],ins[2],ins[3],ins[4]))
        if iday==1:
            thisview.fill(0)
        else:
            thisview -= 1
            np.clip(thisview,0,1000000, thisview)
        
    elif ins[0] == 1:
        # turn on
        print('turning on {0},{1} - {2},{3}'.format(ins[1],ins[2],ins[3],ins[4]))
        if iday == 1:
            thisview.fill(1)
        else:
            thisview += 1
    
    else:
        # toggle
        print('toggling {0},{1} - {2},{3}'.format(ins[1],ins[2],ins[3],ins[4]))
        if iday == 1:
            for li in np.nditer(thisview, op_flags=['readwrite']):
                if (li == 0):
                    li[...] = 1
                else:
                    li[...] = 0
        else:
            thisview += 2
    

lightcount = np.sum(lights)

print('lightcount={0}'.format(lightcount))

plt.pcolor(lights)
plt.show()

        