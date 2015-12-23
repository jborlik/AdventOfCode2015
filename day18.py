# -*- coding: utf-8 -*-

import numpy as np

IPART = 2

class LightMatrix:
    
    def __init__(self):
        self.maxrows = 100
        self.maxcols = 100
        self.lights = np.zeros( (self.maxrows,self.maxcols), dtype=int)
        
    def readCurrentState(self, myfilename):
        with open(myfilename) as datafile:
            irow = 0
            for thisstring in datafile:
                icol = 0
                thisstring = thisstring.rstrip()
                for thischar in thisstring:
                    if (thischar == '#'):
                        self.lights[irow,icol] = 1
                    elif (thischar == '.'):
                        self.lights[irow,icol] = 0
                    else:
                        print("WHAA? {0},{1}:{2}".format(irow,icol,thischar))
                    icol += 1
                irow +=1
    
    def countActiveNeighbors(self, irow, icol):
        neighbors = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        thecount = 0
        for inc_row, inc_col in neighbors:
            neighbor_row = irow + inc_row
            neighbor_col = icol + inc_col
            if (neighbor_row >= self.maxrows) or (neighbor_row < 0):
                continue
            if (neighbor_col >= self.maxcols) or (neighbor_col < 0):
                continue
            #print("---- {0}x{1} inspecting {2}x{3}={4}".format(irow,icol,neighbor_row,neighbor_col,self.lights[neighbor_row,neighbor_col]))
            thecount += self.lights[neighbor_row,neighbor_col]

        return thecount
    
    def makeStep(self):
        global IPART
        
        nextlights = np.copy(self.lights)
        it = np.nditer(self.lights, flags=['multi_index'])
        while not it.finished:
            thisvalue = it[0]
            neighborcount = self.countActiveNeighbors(it.multi_index[0], it.multi_index[1])
            #print("{0}x{1} value {2} neighborcount {3}".format(it.multi_index[0], it.multi_index[1], thisvalue, neighborcount))            
            if thisvalue ==1:
                if (neighborcount == 2) or (neighborcount == 3):
                    # stay on
                    nextlights[it.multi_index[0], it.multi_index[1]] = 1
                else:
                    nextlights[it.multi_index[0], it.multi_index[1]] = 0
            else:
                if neighborcount == 3:
                    nextlights[it.multi_index[0], it.multi_index[1]] = 1
                else:
                    # stay off
                    nextlights[it.multi_index[0], it.multi_index[1]] = 0
            it.iternext()
        if IPART==2:
            nextlights[0,0] = 1
            nextlights[self.maxrows-1,0] = 1
            nextlights[0,self.maxcols-1] = 1
            nextlights[self.maxrows-1,self.maxcols-1] = 1
        self.lights = nextlights
    
if __name__ == "__main__":
    """Day18: Game-of-life"""
    
    print("-----------Testing-----------")
    
    testlights = LightMatrix()
    testlights.maxrows = 6
    testlights.maxcols = 6
    #testlights.lights = np.zeros( (6,6), dtype=int)
    testlights.lights = np.array( [[0,1,0,1,0,1], \
                                  [0,0,0,1,1,0], \
                                  [1,0,0,0,0,1], \
                                  [0,0,1,0,0,0], \
                                  [1,0,1,0,0,1], \
                                  [1,1,1,1,0,0] ], dtype=int)
    
    print(testlights.lights)
    testlights.makeStep()
    print(testlights.lights)
    testlights.makeStep()
    print(testlights.lights)
    
    print("----------Day One -----------")

    lights = LightMatrix()
    lights.readCurrentState('day18.dat')
    
    for i in range(1,101):
        lights.makeStep()
        
        counton = 0
        for thisval in np.nditer(lights.lights):
            counton += thisval
       
        print("After {0} iterations:  {1} on".format(i,counton) )
        
        

    
        
    
