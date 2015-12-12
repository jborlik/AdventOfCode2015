# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

def stringifyPos(position):
    return "{0}x{1}".format(position[0],position[1])



with open('day3.dat') as datafile:
    alldata = datafile.readline()


currpos = ([0,0], [0,0])
maxx = 0
minx = 0
maxy = 0
miny = 0

activesanta = 0

hits = {}
hits['0x0'] = 1

for thisIns in alldata:
    if (thisIns == '^'):
        currpos[activesanta][1] += 1
        if (currpos[activesanta][1] > maxy):
            maxy = currpos[activesanta][1]
    elif (thisIns == 'v'):
        currpos[activesanta][1] -= 1
        if (currpos[activesanta][1] < miny):
            miny = currpos[activesanta][1]
    elif (thisIns == '>'):
        currpos[activesanta][0] += 1
        if (currpos[activesanta][0] > maxx):
            maxx = currpos[activesanta][0]
    elif (thisIns == '<'):
        currpos[activesanta][0] -= 1
        if (currpos[activesanta][0] < minx):
            minx = currpos[activesanta][0]
    if (stringifyPos(currpos[activesanta]) in hits):
        hits[stringifyPos(currpos[activesanta])] += 1
    else:
        hits[stringifyPos(currpos[activesanta])] = 1
    # swap activesanta
    activesanta += 1
    if (activesanta > 0):
        activesanta = 0
    
    
print("Number of houses: {0}".format(len(hits)))
print("x = [{0},{1}], y=[{2},{3}]".format(minx,maxx,miny,maxy))
# for the heck of it, let's plot it

# extract x, y, z

x = np.arange(minx,maxx+1,dtype=int)
y = np.arange(miny,maxy+1,dtype=int)
z = np.zeros( (maxx-minx+1,maxy-miny+1), dtype=int  )


for xystring in hits.keys():
    xylist = xystring.split('x')
    z[  int(xylist[0])-minx   ,  int(xylist[1])-miny  ] = hits[xystring]


zmax = np.max(z)


plt.pcolor(z)
#plt.axis([x.min(), x.max(), y.min(), y.max()])
plt.show()



